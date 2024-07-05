import os
import json
from pydantic import ValidationError
from .models import Timeline
from groq import Groq

# Load the API key from .env file
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('GROQ_API_KEY')
MODEL = 'llama3-70b-8192'
client = Groq(api_key=API_KEY)

def save_timeline(timeline_data):
    try:
        timeline = Timeline(**timeline_data)
        return timeline
    except ValidationError as e:
        return {"error": e.errors()}

def get_timeline_from_groq(user_prompt):
    messages = [
        {
            "role": "system",
            "content": "You are a function calling LLM that saves timelines using the function save_timeline. When prompted to give the timeline for an event, save it using the save_timeline function."
        },
        {
            "role": "user",
            "content": user_prompt,
        }
    ]
    tools = [
        {
            "type": "function",
            "name": "save_timeline",
            "description": "Save a timeline to database.",
            "parameters": {
                "type": "object",
                "properties": {
                    "timeline": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "timestamp": {
                                    "type": "string",
                                    "description": "date of the event"
                                },
                                "title": {
                                    "type": "string",
                                    "description": "title of the event"
                                },
                                "description": {
                                    "type": "string",
                                    "description": "short description of the event"
                                }
                            },
                            "required": ["timestamp", "title", "description"]
                        }
                    }
                },
                "required": ["timeline"]
            }
        }
    ]
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        functions=tools,
        max_tokens=4096
    )

    try:
        response_message = response.choices[0].message
        timeline_data = json.loads(response_message.function_call.arguments)
        result = save_timeline(timeline_data)
        return result
    except Exception as e:
        raise e
