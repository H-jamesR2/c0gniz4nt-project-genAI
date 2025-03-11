from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from uuid import UUID


class TaskBase(BaseModel):
    title: str = Field(..., example="Complete math assignment")
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    priority: int = Field(default=1, ge=1, le=3, example=2)  # 1 = Low, 2 = Medium, 3 = High

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    priority: Optional[int] = Field(None, ge=1, le=3, example=2)
    completed: Optional[bool] = None


class TaskResponse(TaskBase):
    id: UUID
    completed: bool
    created_at: datetime

    class Config:
        from_attributes = True

