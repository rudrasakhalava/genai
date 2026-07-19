from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("Conor_McGregor_Overview.pdf")

docs = loader.load()

print(docs)