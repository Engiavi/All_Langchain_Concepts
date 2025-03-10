from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
ques = input("Enter your question: \n")
result = model.invoke(ques)

print(result.content)