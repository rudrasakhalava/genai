from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOpenAI(model="gpt-5-nano")

paper_input = input("Enter the topic :: ")
length_input = input("Enter the length(short, medium, long) :: ")
style_input = input("Enter the topic(beginner friendly, technical, code-oriented, mathematical) :: ")

template = PromptTemplate(template="""please summarize the topic titled :: {paper_input} with following specification,Explanation length : {length_input} and Explanation style : {style_input}. here Explanation length short means in 3-4 lines.""",
                            input_variables=["paper_input","length_input","style_input"]
                          )

prompt = template.invoke({
    "paper_input" : paper_input, "length_input" : length_input, "style_input" : style_input
})

result = model.invoke(prompt)
print(result.content)
