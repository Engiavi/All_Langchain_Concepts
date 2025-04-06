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
# in the above line we are chaining the output of template1 to model and then take the result of model to send it to parser, parser will parse the output and then send it to template2 and then again send the result to model and then again parser will parse the output

result = chain.invoke({"topic": "Black Hole"})

print(result)