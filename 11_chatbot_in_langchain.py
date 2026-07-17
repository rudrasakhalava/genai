from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

model = ChatOpenAI(model="gpt-5-nano")

chat_history = [
    SystemMessage(content="You are a helpful AI assistant.")
]

while True:
    user = input("YOU :: ")
    chat_history.append(HumanMessage(content=user))

    if user == "exit" :
        chat_history.append(AIMessage(content="Closed"))
        break

    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI :: ",result.content)

print(chat_history)