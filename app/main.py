from fastapi import FastAPI
from .database import engine, Base
from app.routers import tasks

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(tasks.router, prefix='', tags=['Tasks'])
