# utils/llm.py
import os
import getpass
from langchain_google_genai import ChatGoogleGenerativeAI

def getLlm():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        api_key = getpass.getpass("Enter your Google API key: ")
        os.environ["GOOGLE_API_KEY"] = api_key
    
    llm = ChatGoogleGenerativeAI(
        model="gemini-pro",
        google_api_key=api_key
    )
    return llm