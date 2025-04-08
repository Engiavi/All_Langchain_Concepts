from langchain_google_genai import ChatGoogleGenerativeAI  #type: ignore
from langchain.prompts import PromptTemplate #type: ignore
from langchain_core.output_parsers import StrOutputParser #type: ignore
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableParallel,RunnableSequence #type: ignore

load_dotenv()

model = ChatGoogleGenerativeAI(model ="gemini-2.0-flash")#Google Gemini model

parser = StrOutputParser()#string output parser

prompt1 = PromptTemplate(
    template ="write a tweet on topic {topic}",
    input_variables = ["topic"],
)

prompt2 = PromptTemplate(
    template = "write linkedIn post on topic {topic}",
    input_variables = ["topic"],
)

prallel = RunnableParallel({
    'tweet':RunnableSequence(prompt1,model,parser),
    'linkedIn':RunnableSequence(prompt2,model,parser)    
})
result = prallel.invoke({"topic":"AI in 2025"})
print(result['linkedIn'])