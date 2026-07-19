from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

prompt1 = PromptTemplate(
    template="give me one liner joke on {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="give me 2-3 line as a explain on this joke : {joke}",
    input_variables=["joke"]
)

model = ChatOpenAI(model="gpt-5-nano")

parser = StrOutputParser()

chain = RunnableSequence(prompt1,model,parser,RunnableParallel({"joke" : RunnablePassthrough(), "Explanation" : RunnableSequence(prompt2,model,parser)}))

result = chain.invoke({"topic" : "AI"})

print(result)