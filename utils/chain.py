from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from utils.llm import getLlm



prompt=ChatPromptTemplate.from_template("tell me about {topic}")
llm=getLlm()


def setupChain():
    chain=prompt | llm | StrOutputParser()
    print(chain)
    return chain


