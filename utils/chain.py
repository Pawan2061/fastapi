from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_core.runnables import RunnablePassthrough
import os
from langchain_core.output_parsers import StrOutputParser
from utils.llm import getLlm
from langchain_openai import OpenAIEmbeddings
OPENAI_KEY=os.getenv("OPENAI_KEY")
vectorstore=FAISS.from_texts(
    ["harrison worked at kensho"], embedding=OpenAIEmbeddings(api_key=OPENAI_KEY)
)
retriever=vectorstore.as_retriever()

template = """Answer the question based only on the following context:
{context}

Question: {question}
"""



prompt=ChatPromptTemplate.from_template(template=template)

llm=getLlm()


def setupChain():
    
    chain=prompt | llm | StrOutputParser()
    chain = (
    {
        "context": lambda x: (x["context"]),
        "question": lambda x: (x["question"])
    }
    | prompt 
    | llm 
    | StrOutputParser()
)
    print(chain)
    return chain