# utils/llm.py
import os
import getpass
from langchain_openai import ChatOpenAI

def getLlm():
    api_key = os.getenv("OPENAI_KEY")
    if not api_key:
        api_key = getpass.getpass("Enter your Google API key: ")
        os.environ["OPENAI_KEY"] = api_key
    
    llm = ChatOpenAI(
        model="gpt-4o",
        api_key=api_key
        
    )
    return llm

