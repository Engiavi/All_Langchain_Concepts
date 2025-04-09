# https://www.shl.com/solutions/products/product-catalog/
from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI  # type:ignore
from langchain_core.output_parsers import StrOutputParser  # type:ignore
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate  # type:ignore

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
parser = StrOutputParser()
prompt = PromptTemplate(
    template="list the all Pre-packaged Job Solutions and Individual Test Solutions from this content, along with its headings {job}", input_variables=["job"]
)

url = "https://www.shl.com/solutions/products/product-catalog/"
loader = WebBaseLoader(url)

res = loader.load()
chain = prompt | model | parser
result = chain.invoke({"job": res[0].page_content})
print(result)