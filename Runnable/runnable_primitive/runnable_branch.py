from langchain.schema.runnable import RunnableBranch,RunnableSequence,RunnablePassthrough #type:ignore
from dotenv import load_dotenv #type:ignore
from langchain_core.prompts import PromptTemplate #type:ignore
from langchain_google_genai import ChatGoogleGenerativeAI #type:ignore
from langchain_core.output_parsers import StrOutputParser #type:ignore

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
parser = StrOutputParser()

prompt = PromptTemplate(
    template = "write a detailed report on {topic}",
    input_variables =['topic']
)

prompt2 = PromptTemplate(
    template = "summarize the topic {topic}",
    input_variables =['topic']
)

# output1 = RunnableSequence(prompt,model,parser) # with the help of RunnableSequence 

output1 = prompt | model | parser # this is equivalent to the above line also called as LCEL or Chain, execute in similar way as RunnableSequence
branch_chain = RunnableBranch(
    (lambda x: len(x.split())>500,RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(output1,branch_chain)
result = final_chain.invoke({"topic":"AI"})
print(result)
