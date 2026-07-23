from langchain_community.tools import DuckDuckGoSearchRun

tool = DuckDuckGoSearchRun()

result = tool.invoke("top 5 news in india today")

print(result)