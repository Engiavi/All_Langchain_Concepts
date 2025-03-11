from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite")

while True:
    user_input = input("👦🏻: ")
    if user_input == "exit":
        break
    result = model.invoke(user_input)
    print("🤖:",result.content)