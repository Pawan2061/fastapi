# from fastapi import APIRouter,Depends
# from sqlmodel import Session
# from main import engine
# from utils.chain import setupChain
# from database import ChainRequest
# chainRouter=APIRouter()

# chain=setupChain()


# @chainRouter.post("/")

# async def get_ans(request:ChainRequest):
#     print("inside chain")
#     topic = request.topic
#     print("the topic is ",topic)
#     ans = await chain.invoke({"topic": topic})

#     if ans:

#         print("got the ans",ans)
#         return ans
#     else:   
#         print("some problems is here")
#         return "pro"


  


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
