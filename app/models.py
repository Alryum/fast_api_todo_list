from sqlalchemy import Column, Integer, String, Enum
from .database import Base
import enum

class TaskStatus(str, enum.Enum):
    todo = 'todo'
    in_progress = 'in_progress'
    done = 'done'

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    status = Column(Enum(TaskStatus), default=TaskStatus.todo)
