from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ValidationError, Field
from typing import List
import os
import json
from .groq_client import get_timeline_from_groq

app = FastAPI()

class TimelineEvent(BaseModel):
    timestamp: str = Field(..., description="Date of the event")
    title: str = Field(..., description="Title of the event")
    description: str = Field(..., description="Short description of the event")

class Timeline(BaseModel):
    timeline: List[TimelineEvent]

@app.get("/get_timeline")
def get_timeline(user_prompt: str):
    try:
        result = get_timeline_from_groq(user_prompt)
        return result
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=e.errors())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
