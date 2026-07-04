from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.responses.create(
    model="gpt-5-nano",
    max_output_tokens=1000,
    input="Explain Machine Learning in 3-4 lines."
)

print(response.output_text)