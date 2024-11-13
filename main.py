from fastapi import FastAPI
from database import create_database,User,engine
from contextlib import asynccontextmanager

from sqlmodel import Session






@asynccontextmanager
async def lifespan(app:FastAPI):
    create_database()
    yield

app=FastAPI(lifespan=lifespan)

    
@app.get("/")
async def root():
    print("hello")
    return {"message":"hello world"}


@app.post("/createuser")
def create_user(user:User):
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)

        return session  


