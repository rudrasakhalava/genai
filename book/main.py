from fastapi import FastAPI
from models import text_generation

app = FastAPI()

@app.get("/generation/text")
def serve_llm(prompt : str) -> str:

    out = text_generation(prompt)

    return out