from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-5-nano")

result = model.invoke("What is the capital of india? give answer in just one line")

print(result.content)