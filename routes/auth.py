from fastapi import APIRouter
from database import User
from sqlmodel import Session,select
from main import engine
userrouter=APIRouter()


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

        return user
