from langchain_google_genai import ChatGoogleGenerativeAI # type: ignore
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser # type: ignore
from langchain_core.prompts import PromptTemplate # type: ignore

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite")
parser = JsonOutputParser()
template = PromptTemplate(
    template= 'Give the name, age and city of any indian fictional person \n{format_instructions}',
    input_variables=[],
    partial_variables={'format_instructions': parser.get_format_instructions()},
)
# the working of above lines of code is that
# 1. we are creating a prompt template with the template and input variables
# 2. we are passing the format instructions to the prompt template
# 3. we are creating a parser with the JsonOutputParser
# 4. we are passing the parser to the prompt template

# prompt = template.format()

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

# these above line can be use in single line using chain

chain  = template | model | parser
result = chain.invoke({}) #we have to send input variables, but in template we haven't send any input thus we are sending empty dictionary
print(result)
print(type(result))