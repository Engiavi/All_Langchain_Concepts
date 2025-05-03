from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
import requests
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from dotenv import load_dotenv
load_dotenv()

# built-in tool- it is a search tool which is used to search the web for information. It uses the DuckDuckGo search engine to perform the search and returns the results in a structured format.
search_tool = DuckDuckGoSearchRun() 