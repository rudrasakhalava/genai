from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

with client.responses.stream(
    model="gpt-5-nano",
    input="Explain Machine Learning in just 2-3 lines."
) as stream:

    for event in stream:
        if event.type == "response.output_text.delta":
            print(event.delta, end="")