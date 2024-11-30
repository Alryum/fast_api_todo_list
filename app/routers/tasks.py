from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import get_db

router = APIRouter()

@router.post('/tasks/', response_model=schemas.TaskResponse)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)

@router.get('/tasks/', response_model=list[schemas.TaskResponse])
def read_tasks(status: schemas.TaskStatus = None, db: Session = Depends(get_db)):
    return crud.get_tasks(db, status)

@router.get('/tasks/{task_id}/', response_model=schemas.TaskResponse)
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail='Task not found')
    return task

@router.put('/tasks/{task_id}/', response_model=schemas.TaskResponse)
def update_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    updated_task = crud.update_task(db, task_id, task)
    if not updated_task:
        raise HTTPException(status_code=404, detail='Task not found')
    return updated_task

@router.delete('/tasks/{task_id}/', response_model=schemas.TaskResponse)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.delete_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail='Task not found')
    return task
