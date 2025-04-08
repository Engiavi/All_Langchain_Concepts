from langchain_google_genai import ChatGoogleGenerativeAI  #type: ignore
from langchain.prompts import PromptTemplate #type: ignore
from langchain_core.output_parsers import StrOutputParser #type: ignore
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence #type: ignore

load_dotenv()#load env variables from .env file
model = ChatGoogleGenerativeAI(model ="gemini-2.0-flash")#Google Gemini model

parser = StrOutputParser()#string output parser

prompt =PromptTemplate( #prompt template
    template = "write a joke about {text}",
    input_variables = ["text"],
) 

prompt2 = PromptTemplate(
    template = "Explain the provided joke {text}",
    input_variables = ["text"],
)
 
chain = RunnableSequence(prompt,model,parser,prompt2,model,parser)
# it performs the above chain like this prompt's output->(prompt's output becomes input) model's output->(model's output becomes input)parser

result = chain.invoke({"text":"What is the capital of France?"})

print(result)