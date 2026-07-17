from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-5-nano")

chat_history = []

while True:
    user = input("YOU :: ")
    chat_history.append(user)

    if user == "exit" :
        chat_history.append("Closed")
        break

    result = model.invoke(chat_history)
    chat_history.append(result.content)
    print("AI :: ",result.content)

print(chat_history)