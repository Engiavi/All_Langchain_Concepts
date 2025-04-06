from langchain_google_genai import ChatGoogleGenerativeAI # type: ignore
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate # type: ignore
from langchain.output_parsers import StructuredOutputParser, ResponseSchema # type: ignore
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite")

schema = [
    ResponseSchema(name="Fact-1",description ="The first fact about the topic"),
    ResponseSchema(name="Fact-2",description ="The second fact about the topic"),
    ResponseSchema(name="Fact-3",description ="The third fact about the topic")
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='Give me 3 facts about {topic} \n {format_instructions}',
    input_variables=['topic'],
    partial_variables={'format_instructions': parser.get_format_instructions()},
)
# prompt = template.invoke({'topic':"Black Hole"})
# result = model.invoke(prompt)
# final_result = parser.parse(result.content)
chain = template | model | parser
result = chain.invoke({'topic':"Black Hole"})
print(result)