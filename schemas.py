from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum

class StatusEnum(str, Enum):
    pending = "pending"
    answered = "answered"

class DocumentCreate(BaseModel):
    title: str
    content: str

class DocumentResponse(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        orm_mode = True

class QuestionCreate(BaseModel):
    question: str

class QuestionResponse(BaseModel):
    id: int
    document_id: int
    question: str
    status: StatusEnum
    answer: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True
