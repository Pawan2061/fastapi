
  


from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from utils.chain import setupChain
from pydantic import BaseModel
from database import ChainRequest

chain = setupChain()



chainRouter = APIRouter()

@chainRouter.post("/")
async def get_ans(request: ChainRequest):
    print("Inside chain")
    topic = request.topic
    print(f"The topic is {topic}")

    try:
        ans =  chain.invoke({"topic": topic})

        if ans:
            print(f"Got the answer: {ans}")
            return ans
        else:
            raise HTTPException(status_code=500, detail="No answer returned from LLM.")
    except Exception as e:
        print(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
