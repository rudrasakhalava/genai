from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langchain_core.messages import HumanMessage

load_dotenv()

@tool
def multiply(a : int, b :int) -> int:
    """Take two numbers a and b and return multiplication of that two numbers"""
    return a * b

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0.2)

llm_with_tool = llm.bind_tools([multiply])

que = input("You :: ")

query = HumanMessage(que)

messages = [query]

result = llm_with_tool.invoke(messages)
messages.append(result)

ans = multiply.invoke(result.tool_calls[0])
messages.append(ans)

final_ans = llm_with_tool.invoke(messages).content
print(f"AI :: {final_ans}")
