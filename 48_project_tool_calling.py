from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.tools import tool
import requests
from langchain_core.messages import HumanMessage

load_dotenv()

@tool
def currency_converter(amount : float, from_currency : str, to_currency : str) -> float :
    """
    Convert one currency to another using live exchange rates.
    """

    url = (
        f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency.upper()}&to={to_currency.upper()}"
    )

    response = requests.get(url)
    data = response.json()

    return data["rates"][to_currency.upper()]

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0.2)

llm_with_tool = llm.bind_tools([currency_converter])

que = input("You :: ")

query = HumanMessage(que)

messages = [query]

result = llm_with_tool.invoke(messages)
messages.append(result)

ans = currency_converter.invoke(result.tool_calls[0])
messages.append(ans)

final_ans = llm_with_tool.invoke(messages).content
print(f"AI :: {final_ans}")