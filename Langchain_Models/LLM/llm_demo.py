from langchain_openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import os

llm = OpenAI(model='gpt-3.5-turbo-instruct', api_key=os.getenv ('OPENAI_API_KEY'))

llm.invoke("What is the capital of India?") #invoke is use to call the model and ask the question, if it gives output then it is working fine

# whole working of above code
# 1. First we import OpenAI from langchain_openai and load_dotenv from dotenv
# 2. Then we load the .env file using load_dotenv()
# 3. Then we create an object of OpenAI and pass the model name and api_key as an argument
# 4. Then we call the invoke method and pass the question as an argument
# 5. If the output is generated then the code is working fine

