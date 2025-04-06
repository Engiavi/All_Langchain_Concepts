from langchain_core.output_parsers import PydanticOutputParser #type: ignore
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate #type:ignore
from langchain_google_genai import ChatGoogleGenerativeAI #type:ignore
from pydantic import BaseModel, Field #type:ignore

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite")

class Person(BaseModel):
    name: str = Field(description="Name of the person")
    age: int = Field(gt =18  ,description="Age of the person")
    city: str = Field(description="City of the person")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template= 'Give the name, age and city of any fictional {place} person \n{format_instructions}',
    input_variables=['place'],
    partial_variables={'format_instructions': parser.get_format_instructions()},
)

chain = template | model | parser
result = chain.invoke({'place':"indian"})
print(result)