from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

template1 = PromptTemplate(
    template="write in detail report on the topic {topic}",
    input_variables=["topic"]
)

template2 = PromptTemplate(
    template="on the basis of this report, give 5 line summary {text}",
    input_variables=["text"]
)

model = ChatOpenAI(model="gpt-5-nano")

parse = StrOutputParser()

chain = template1 | model | parse | template2 | model | parse

result = chain.invoke({"topic" : "black hole"})

print(result)