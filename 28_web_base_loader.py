from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://en.wikipedia.org/wiki/Conor_McGregor")

docs = loader.load()

print(docs)