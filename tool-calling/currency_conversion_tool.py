# as llm does not provide real time conversion of currency. this tools helps to create a real time conversion based on tool function and then it will be interact with LLM to provide a language generation.

# this tool hit an api and provide real - time currency conversion

# tool create
from langchain_core.tools import InjectedToolArg
from typing import Annotated
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage #HumanMessage represents messages from a human user, while ToolMessage is used to convey the results of executing a tool by the AI. 
import requests
from dotenv import load_dotenv
load_dotenv()

@tool
def get_conversion_factor(base_currency: str, target_currency: str) -> float:
  """
  This function fetches the currency conversion factor between a given base currency and a target currency
  """
  url = f'https://v6.exchangerate-api.com/v6/59842f1da63f8f5fad2b6299/pair/{base_currency}/{target_currency}'

  response = requests.get(url)

  return response.json()

@tool
def convert(base_currency_value: int, conversion_rate: Annotated[float, InjectedToolArg]) -> float:
  """
  given a currency conversion rate this function calculates the target currency value from a given base currency value
  """

  return base_currency_value * conversion_rate

print(get_conversion_factor.invoke({'base_currency':'USD','target_currency':'INR'}))