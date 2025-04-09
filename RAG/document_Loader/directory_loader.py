from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path = "books", #directory name
    glob ="*.pdf", # which file to be loaded
    loader_cls =PyPDFLoader #the subfile format if it is text then use text-loader
)
# docs = loader.lazy_load()
docs = loader.load()

print(len(docs))
print(docs[42].page_content)
print(docs[42].metadata)

# load vs lazy_load
# these methods can be easliy used with load but not with lazy_load
# print(len(docs)) //->because lazy_load is a generator
# print(docs[42].page_content) // generator' object is not subscriptable
# print(docs[42].metadata)

# lazy_load is use when you have large number of files and you want to load them in chunks, at once