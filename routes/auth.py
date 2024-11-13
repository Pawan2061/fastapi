from fastapi import APIRouter
from database import User
from sqlmodel import Session,select
from datetime import timedelta
from utils.jwt import create_access_token
from main import engine
from dotenv import load_dotenv
import os
userrouter=APIRouter()

load_dotenv()

@userrouter.get("/",tags=["check"])
async def check_route():
    return{
        "message":"healthy route"
    }


@userrouter.get("/hello",tags=["doublecheck"])
async def check_hello():
    return{
        "message":"healthy again"
    }


@userrouter.post("/signup")
async def signup(user:User)-> User:
    with Session(engine) as session:
        print(user)
        session.add(user)
        session.commit()
        session.refresh(user)
        access_token_expires = timedelta(minutes=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")))


        access_token = create_access_token(
        data={"sub": user.name}, expires_delta=access_token_expires
       
    )
        print(access_token)
        return user
@userrouter.get("/getusers")
async def getUsers():
    with Session(engine) as session:
        users=session.exec(select(User)).all()
        return users
    

@userrouter.get('/getUsers/{user_id}')
async def getUser(user_id:int):
    with Session(engine) as session:
        user = session.exec(select(User).where(User.id == user_id)).first()

        if(user):
            print(f"user found: {user}")

        return user
