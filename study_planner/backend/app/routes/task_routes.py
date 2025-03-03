from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from app.schemas.task_schema import TaskCreate, TaskUpdate, TaskResponse
from app.services.task_service import create_task, get_tasks, update_task, delete_task
from typing import List, Optional
from uuid import UUID


router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/", response_model=TaskResponse)
def create_new_task(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(db, task)

@router.get("/", response_model=List[TaskResponse])
def read_tasks(completed: Optional[bool] = None, db: Session = Depends(get_db)):
    return get_tasks(db, completed)

@router.put("/{task_id}", response_model=TaskResponse)
def modify_task(task_id: UUID, task_update: TaskUpdate, db: Session = Depends(get_db)):
    updated_task = update_task(db, task_id, task_update)
    if updated_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

@router.delete("/{task_id}")
def remove_task(task_id: UUID, db: Session = Depends(get_db)):
    deleted_task = delete_task(db, task_id)
    if deleted_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": f"Task {task_id} deleted successfully"}

