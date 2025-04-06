from langchain_google_genai import ChatGoogleGenerativeAI # type: ignore
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate # type: ignore
from langchain_core.output_parsers import StrOutputParser # type: ignore

load_dotenv()
model  = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
parser = StrOutputParser()
template1 = PromptTemplate(
    template='write some intersting facts in detail about {topic}',
    input_variables=['topic']
)
template2 = PromptTemplate(
    template='write characterstics on {topic}',
    input_variables=['topic']
)

chain = template1 | model | parser | template2 | model | parser  
result = chain.invoke({"topic": "Buggati"})
print(result)

chain.get_graph().print_ascii()