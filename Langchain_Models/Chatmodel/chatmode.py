from langchain_openai import ChatOpenAI
# ChatOpenAI is inherited from BaseChatModel
# while OpenAI is inherited from BaseLLM
from dotenv import load_dotenv
load_dotenv()

chatModel=ChatOpenAI(model="gpt-4")

result = chatModel.invoke("what is the capital of India?")

print(result)

# in LLM code we get only the string says "New Delhi", but here we get the whole response from the model
# like content="the capital of India is New Delhi", additionally it contains various other information
