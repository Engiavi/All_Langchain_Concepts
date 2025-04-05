from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate,PromptTemplate

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

prompt1 = template1.invoke({'topic':"what is black hole"})

result = model.invoke(prompt1)

prompt2 = template2.invoke({'text':result.content})

result2 = model.invoke(prompt2)
print(result2.content)
