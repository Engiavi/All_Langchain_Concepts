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
import json
from langchain.agents import initialize_agent, AgentType
load_dotenv()
# what is the use of InjectedToolArg? 
# InjectedToolArg is used to inject the value of a tool argument into the function signature. This allows the function to accept the value of the argument directly, rather than having to extract it from the tool call. in simple words, it suggest llm that this field is injected by user only/ after getting response. if the field is missing then you don't have permission to fill it.
@tool
def get_conversion_factor(base_currency: str, target_currency: str) -> float:
  """
  This function fetches the currency conversion factor between a given base currency and a target currency
  """
  url = f'https://v6.exchangerate-api.com/v6/59842f1da63f8f5fad2b6299/pair/{base_currency}/{target_currency}'

  response = requests.get(url)

  return response.json()

@tool
def convert(base_currency_value: float, conversion_rate: Annotated[float, InjectedToolArg]) -> float:
  """
  given a currency conversion rate this function calculates the target currency value from a given base currency value
  """

  return base_currency_value * conversion_rate
# examples:-
# response = get_conversion_factor.invoke({'base_currency':'USD','target_currency':'INR'})
# conversion_rate = response['conversion_rate']
# print(convert.invoke({'base_currency_value':10, 'conversion_rate':conversion_rate}))

# tool binding(bind the tools with the LLM)

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
llm_with_tools = llm.bind_tools([get_conversion_factor, convert])

# Human message
messages = [HumanMessage('What is the conversion factor between USD and INR, and based on that can you convert 10 usd to inr')]

# print(messages)

ai_message = llm_with_tools.invoke(messages)
messages.append(ai_message)
# print(messages)
# print("\n")
# print(ai_message.tool_calls)
#tool calling and tool execution
for tool_call in ai_message.tool_calls:
  # execute the 1st tool and get the value of conversion rate
  if tool_call['name'] == 'get_conversion_factor':
    tool_message1 = get_conversion_factor.invoke(tool_call)
    
    # fetch this conversion rate
    conversion_rate = json.loads(tool_message1.content)['conversion_rate']
    # append this tool message to messages list
    messages.append(tool_message1)
  # execute the 2nd tool using the conversion rate from tool 1
  if tool_call['name'] == 'convert':
    # fetch the current arg
    tool_call['args']['conversion_rate'] = conversion_rate
    tool_message2 = convert.invoke(tool_call)
    print(tool_message2)
    messages.append(tool_message2)
    
print(llm_with_tools.invoke(messages).content)
