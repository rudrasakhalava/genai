from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template="give me the 5 lines of explainantion of {topic}",
    input_variables=["topic"]
)

model = ChatOpenAI(model="gpt-5-nano")

parse = StrOutputParser()

chain = prompt | model | parse

result = chain.invoke({"topic" : "black hole"})

print(result)