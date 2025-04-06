# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional,Literal 
from langchain_anthropic import ChatAnthropic # type: ignore
from dotenv import load_dotenv

load_dotenv()
model = ChatAnthropic(model="claude-3-7-sonnet-20250219")

# load_dotenv()
# # using the LLM chatmodel
# model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite")

# schema for the response
class Review(TypedDict):
    key_themes: Annotated[str, "key themes of the review"]
    summary: Annotated[str,"a breif summary of the review"]
    sentiment: Annotated[str, "write sentiment of the review which is either negative, positive or neutral"]
    pros:Annotated[Optional[Literal["P","N"]],"After analyzing the text write review only in P or N"]
    
# with structured output
structured_model = model.with_structured_output(Review)

# invoke the structured model instead of LLM chatmodel
result = structured_model.invoke("""The hardware is great, but the software feels bloated. There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this.""")

print(result)