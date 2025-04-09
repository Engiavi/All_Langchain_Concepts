# all document loaders resides in langchain_community.document_loaders
from langchain_community.document_loaders import TextLoader  # type:ignore
from langchain_google_genai import ChatGoogleGenerativeAI  # type:ignore
from langchain_core.output_parsers import StrOutputParser  # type:ignore
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate  # type:ignore

loader = TextLoader("cricket.txt", encoding="utf-8")
load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
parser = StrOutputParser()
docs = loader.load()
# when loading the any document loader, then it seems to have list.
# if we print the length of the docs, it will be 1
# after loading it contains two things page_content and metadata
# we can access the content by using docs[0]
# now by doing docs[0].page_content, we can access the content of the document
# we can also access the metadata by using docs[0].metadata


prompt = PromptTemplate(
    template="Extract 5 keyword on topic {topic}", input_variables=["topic"]
)

chain = prompt | model | parser
result = chain.invoke({"topic": docs[0].page_content})
print(result)
