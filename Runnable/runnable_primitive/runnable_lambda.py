from langchain_google_genai import ChatGoogleGenerativeAI  #type: ignore
from langchain.prompts import PromptTemplate #type: ignore
from langchain_core.output_parsers import StrOutputParser #type: ignore
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnableLambda, RunnableParallel, RunnablePassthrough #type: ignore

load_dotenv()#load env variables from .env file
model = ChatGoogleGenerativeAI(model ="gemini-2.0-flash")#Google Gemini model

parser = StrOutputParser()

prompt = PromptTemplate(
    template = "write a joke about {text}",
    input_variables = ["text"],
)
def counter(str):
    return len(str.split())

joke_gen_ai = RunnableSequence(prompt,model,parser)

parallel = RunnableParallel({
    "joke": RunnablePassthrough(),
    "length": RunnableLambda(counter),
})

final_chain = RunnableSequence(joke_gen_ai,parallel)
result = final_chain.invoke({"text":"Elephant"})
final_result ="""{}\nWord count:{}""".format(result["joke"],result["length"])
print(final_result)