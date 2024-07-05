from pydantic import BaseModel, Field
from typing import List

class TimelineEvent(BaseModel):
    timestamp: str = Field(..., description="Date of the event")
    title: str = Field(..., description="Title of the event")
    description: str = Field(..., description="Short description of the event")

class Timeline(BaseModel):
    timeline: List[TimelineEvent]
