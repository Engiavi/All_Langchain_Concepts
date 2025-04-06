from langchain_google_genai import ChatGoogleGenerativeAI # type: ignore
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate # type: ignore
from langchain_core.output_parsers import StrOutputParser # type: ignore

load_dotenv()

model  = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
parser = StrOutputParser()
template = PromptTemplate(
    template='write some intersting facts about {topic}',
    input_variables=['topic']
)

chain = template | model| parser #langchain expression language (LCA)
result = chain.invoke({"topic": "Black Hole"})
print(result) 

#visualize the chain
chain.get_graph().print_ascii()