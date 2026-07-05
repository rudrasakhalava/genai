from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

for chunk in client.models.generate_content_stream(
    model="gemini-2.5-flash",
    contents="Explain LLMs in 2-3 lines."
):
    print(chunk.text, end= "")
