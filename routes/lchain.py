from fastapi import APIRouter, HTTPException
from utils.chain import setupChain
from database import ChainRequest

chain = setupChain()



chainRouter = APIRouter()

@chainRouter.post("/")
async def get_ans(request: ChainRequest):
    print("Inside chain")
    context=request.context
    question = request.question
    
    print(f"The topic is {question}")
    input_data={
        "context":context,
        "question":question
    }
 
    try:
        
        ans =  chain.invoke(input_data)
        print("got the ans")
        for chunk in chain.stream(input_data):
            print(chunk,end="|",flush=True)

        if ans:
            print(f"Got the answer: {ans}")
            return ans
        else:
            raise HTTPException(status_code=500, detail="No answer returned from LLM.")
    except Exception as e:
        print(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
