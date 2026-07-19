from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence

load_dotenv()

prompt = PromptTemplate(
    template="give me one liner joke on {topic}",
    input_variables=["topic"]
)

model = ChatOpenAI(model="gpt-5-nano")

parser = StrOutputParser()

chain = RunnableSequence(prompt,model,parser)

result = chain.invoke({"topic" : "AI"})

print(result)
