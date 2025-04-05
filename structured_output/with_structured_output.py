from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict  

load_dotenv()
# using the LLM chatmodel
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite")

# schema for the response
class Review(TypedDict):
    
    summary: str
    sentiment: str
    
# with structured output
structured_model = model.with_structured_output(Review)


# invoke the structured model instead of LLM chatmodel
result = structured_model.invoke("""The hardware is great, but the software feels bloated. There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this.""")

print(result)