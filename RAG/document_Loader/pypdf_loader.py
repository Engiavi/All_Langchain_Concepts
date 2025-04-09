from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
parser = StrOutputParser()
loader = PyPDFLoader("C++_STL_Interview_Topics.pdf")
prompt = PromptTemplate(
    template="Read out the following text and summarise it {docs}",
    input_variables=["docs"],
)

result = loader.load()
# print(len(result))
print(result[0].page_content)
