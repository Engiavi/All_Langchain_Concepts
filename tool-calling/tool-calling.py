from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests
from dotenv import load_dotenv
load_dotenv()
#tool create
@tool
def multiply(a: int, b: int) -> int:
  """Given 2 numbers a and b this tool returns their product"""
  return a * b

print(multiply.invoke({'a':3, 'b':4}))

llm = ChatGoogleGenerativeAI(model = "gemini-2.0-flash")
llm_with_tools = llm.bind_tools([multiply])

print(llm_with_tools.invoke('Hi how are you'))