from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task_schema import TaskCreate, TaskUpdate
import datetime
from uuid import UUID

def create_task(db: Session, task_data: TaskCreate):
    new_task = Task(
        title=task_data.title,
        description=task_data.description,
        due_date=task_data.due_date,
        priority=task_data.priority,
        completed=False,
        created_at=datetime.datetime.utcnow(),
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def get_tasks(db: Session, completed: bool = None):
    query = db.query(Task)
    if completed is not None:
        query = query.filter(Task.completed == completed)
    return query.all()

def update_task(db: Session, task_id: UUID, task_update: TaskUpdate):
    task = db.query(Task).filter(Task.id == str(task_id)).first()
    if not task:
        return None


    task_data = task_update.dict(exclude_unset=True)
    if not task_data:
        return task  # No update needed

    for key, value in task_data.items():
        setattr(task, key, value)

    db.commit()
    db.refresh(task)
    return task

def delete_task(db: Session, task_id: UUID):
    task = db.query(Task).filter(Task.id == str(task_id)).first()
    if not task:
        return None
    db.delete(task)
    db.commit()
    return task
