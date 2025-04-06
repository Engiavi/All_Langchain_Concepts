from langchain_google_genai import ChatGoogleGenerativeAI # type: ignore
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser # type: ignore
from langchain_core.prompts import PromptTemplate # type: ignore

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite")

template1 = PromptTemplate(
    template ='Write a detailed report on topic {topic}',
    input_variables=['topic'],
)

template2 = PromptTemplate(
    template='Write a 5 line on {text}',
    input_variables=['text'],
)

parser = StrOutputParser() # this will parse the output of the model and convert it to string

chain = template1 | model | parser | template2 | model | parser
# chain is basically chaning the output of one model to the input of another model
# execution of the chain will be like this
# template1 generates a prompt
# model generates a response
# parser parses the response to string
# template2 generates a prompt
# model generates a response
# parser parses the response to string

result = chain.invoke({"topic": "Black Hole"} )

print(result)