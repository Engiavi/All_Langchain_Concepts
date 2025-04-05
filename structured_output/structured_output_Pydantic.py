from pydantic import BaseModel,Field
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import Optional,Literal
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite")

class Review(BaseModel):
    summary :str = Field(description="explain in 5 words in a sentence")
    sentiment :Literal["P","N","T"] =Field(description="write sentiment of the review which is either negative, positive or neutral")
    #  summary: Annotated[str,"a breif summary of the review"]
    # sentiment: Annotated[str, "write sentiment of the review which is either negative, positive or neutral"]

StrucuturedOutput = model.with_structured_output(Review)
# invoke the structured model instead of LLM chatmodel
result = StrucuturedOutput.invoke("""The hardware is great, but the software feels bloated. There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this.""")
print(dict(result))
