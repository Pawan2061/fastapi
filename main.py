from fastapi import FastAPI
from database import create_database,User,engine
from contextlib import asynccontextmanager

from sqlmodel import Session
from routes.auth import userrouter





@asynccontextmanager
async def lifespan(app:FastAPI):
    create_database()
    yield

app=FastAPI(lifespan=lifespan)

app.include_router(userrouter,prefix="/auth",tags=["auth"])

    



