from langchain_community.tools import DuckDuckGoSearchRun

search_tools = DuckDuckGoSearchRun()

result = search_tools.invoke("IPL news")

print(result)