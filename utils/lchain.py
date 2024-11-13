import getpass
import os


os.getenv("OPENAI_KEY")=getpass.getpass()
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from chain import chain

llm=ChatGoogleGenerativeAI(model="gemini-pro",api_key=os.getenv("OPENAI_KEY"))




