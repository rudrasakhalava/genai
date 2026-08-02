from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

def text_generation(prompt : str) -> str:

    llm = ChatOpenAI(model="gpt-5-nano")

    ans = llm.invoke(f"give the answer in just 2-3 lines of this query :: {prompt}")

    parser = StrOutputParser()

    result = parser.invoke(ans)

    return result
    