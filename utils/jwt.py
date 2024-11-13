from datetime import datetime ,timedelta,timezone
from fastapi import Depends,HTTPException,status
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer
import jwt
import os
load_dotenv()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, os.getenv("SECRET_KEY"), algorithm=os.getenv("ALGORITHM"))
    return encoded_jwt



def verify_token(token:str=Depends(oauth2_scheme)):
    try:
        payload=jwt.decode(token,os.getenv("SECRET_KEY"),algorithms=os.getenv("ALGORITHM"))
        user_id:int=payload.get("sub")
        if user_id is None: raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        user={"user_id":user_id}
        return user

    except KeyError:
        raise  HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="couldnot authorized",
            headers={"WWW-Authenticate": "Bearer"},
        )
    

    