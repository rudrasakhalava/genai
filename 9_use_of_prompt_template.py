from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import load_prompt

load_dotenv()

model = ChatOpenAI(model="gpt-5-nano")

paper_input = input("Enter the topic :: ")
length_input = input("Enter the length(short, medium, long) :: ")
style_input = input("Enter the topic(beginner friendly, technical, code-oriented, mathematical) :: ")

template = load_prompt("template.json")

chain = template | model

result = chain.invoke({
    "paper_input" : paper_input, "length_input" : length_input, "style_input" : style_input
})

print(result.content)
