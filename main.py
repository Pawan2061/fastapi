from fastapi import FastAPI
import os
from database import create_database,User,engine
from contextlib import asynccontextmanager
from dotenv import load_dotenv


from sqlmodel import Session
load_dotenv()
from routes.auth import userrouter






@asynccontextmanager
async def lifespan(app:FastAPI):
    create_database()
    yield

app=FastAPI(lifespan=lifespan)

app.include_router(userrouter,prefix="/auth",tags=["auth"])

    



