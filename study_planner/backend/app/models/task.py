import uuid
from sqlalchemy import Integer, Column, String, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.dialects.sqlite import BLOB  # For SQLite compatibility

import datetime
from db.session import Base  # Import Base from db/session.py


class Task(Base):
    __tablename__ = 'tasks'

    #id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    due_date = Column(DateTime, nullable=True)
    priority = Column(Integer, nullable=False, default=1)  # 1 = Low, 2 = Medium, 3 = High
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)

