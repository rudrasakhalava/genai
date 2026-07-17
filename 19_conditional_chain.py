from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatOpenAI(model="gpt-5-nano")

class Feedback(BaseModel):
    sentiment : Literal["positive","negative"] = Field(description="give the sentiment of the feedback")

parser = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template="Classify the sentiments of the following feedback text into positive or negative \n {text} \n {format_instruction}",
    input_variables=["text"],
    partial_variables={"format_instruction" : parser.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser

parser1 = StrOutputParser()

prompt2 = PromptTemplate(
    template="write the appropriate answer on this positive feedback in just 2-3 lines :: \n {text} ",
    input_variables=["text"]
)

prompt3 = PromptTemplate(
    template="write the appropriate answer on this negative feedback in just 2-3 lines :: \n {text} ",
    input_variables=["text"]
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == "positive", prompt2 | model | parser1),
    (lambda x:x.sentiment == "negative", prompt3 | model | parser1),
    RunnableLambda(lambda x: "could not find the sentiment")
)

chain = classifier_chain | branch_chain

result = chain.invoke({"text" : "this is a wonderful phone"})

print(result)
