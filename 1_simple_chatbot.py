from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def ai(input):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=input
    )

    return response.text

while True:
    user = input("You :: ")
    if user.lower() == "exit":
        break
    res = ai(user)
    print("AI :: ",res)