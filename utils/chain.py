from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from lchain import llm



prompt=ChatPromptTemplate.from_template("tell me about {topic}")

chain= prompt.pipe(llm).pipe( StrOutputParser)