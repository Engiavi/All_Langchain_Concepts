from langchain_google_genai import ChatGoogleGenerativeAI # type: ignore
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate # type: ignore
from langchain_core.output_parsers import StrOutputParser # type: ignore
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda # type: ignore
# runnablelambda is used to create a lambda function that can be used in the chain
from langchain_core.output_parsers import PydanticOutputParser # type: ignore
# here we use pydantic output parser, BaseModel,Field and Literal for getting the output in consistent format, either positive,negative or neutral only. 
from pydantic import BaseModel, Field # type: ignore
from typing import Literal

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
parser = StrOutputParser()

class Feedback(BaseModel): # declare class for getting the output in consistent format
    sentiment :Literal['Positive','Negative','Neutral'] = Field(description="The sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object=Feedback) # this is the pydantic output parser that takes object of Feedback class
prompt1 = PromptTemplate(
    template= "Classify the sentiment on the following text either positive, negative or neutral \n {feedback} \n {format_instruction}",
    input_variables=["feedback"],
    partial_variables={"format_instruction": parser2.get_format_instructions()}
)
# we use format_instruction to get the output in the format we want
# partial_variables is used to pass the format_instruction to the prompt, it is not mandatory to use it, we can also pass it in the input variables
classifier_chain = prompt1 | model | parser2
 
# Now we will create branch chain using RunnableBranch
# RunnableBranch is used to create a branch chain, it takes a dictionary as input, where the key is the name of the branch and the value is the chain that will be executed in that branch
# we basically send multiple tuples
#  Runnable( (condition_1,chain1),(condition_2,chain2),default_condition) if condition_1 is true then chain1 will be executed and same as condition_2. if neither of above two conditions are not executed then default_condition will be executed.
prompt2 = PromptTemplate(
    template="generate an appropriate and concise, as well as single response to this positive feedback \n {feedback}",
    input_variables=["feedback"],
)
prompt3 = PromptTemplate(
    template="generate an appropriate and concise, as well as single response to this negative feedback \n {feedback}",
    input_variables=["feedback"],
)
prompt4 = PromptTemplate(
    template="generate an appropriate and concise, as well as single response to this neutral feedback \n {feedback}",
    input_variables=["feedback"],
)

branch = RunnableBranch(
    (lambda x: x.sentiment == "Positive", prompt2 | model | parser),
    (lambda x: x.sentiment == "Negative", prompt3 | model | parser),
    (lambda x: x.sentiment == "Neutral", prompt4 | model | parser),
    RunnableLambda(lambda x: f"Sorry, I cannot respond to this feedback: {x.feedback}"), # default condition
)

chain = classifier_chain | branch
result = chain.invoke({"feedback": "i don't know about this product "})
print(result)

chain.get_graph().print_ascii() # visualize the chain