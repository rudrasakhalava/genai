from langchain_community.document_loaders import TextLoader

loader = TextLoader("conor_mcgregor.txt",encoding="utf-8")

docs = loader.load()

print(docs[0])