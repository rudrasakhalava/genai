from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=32)

doc = [
    "Delhi is the capital of India.",
    "Paris is the capital of France."
]

result = embedding.embed_documents(doc)

print(str(result))