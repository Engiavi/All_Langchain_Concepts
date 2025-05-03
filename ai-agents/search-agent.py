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

# tool decorator
@tool
# it basically give response of the weather data from the weatherstack API
def get_weather_data(city: str) -> str:
  """
  This function fetches the current weather data for a given city
  """
  url = f'https://api.weatherstack.com/current?access_key=4d1d8ae207a8c845a52df8a67bf3623e&query={city}'

  response = requests.get(url)

  return response.json()