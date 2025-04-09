from langchain.text_splitter import CharacterTextSplitter # importing the CharacterTextSplitter class
from langchain_community.document_loaders import PyPDFLoader # importing the PyPDFLoader class to load the pdf file

url = "books/C++_STL_Interview_Topics.pdf"

spliter = CharacterTextSplitter(chunk_size=50, chunk_overlap=0,separator="") # creating an instance of the CharacterTextSplitter class
loader = PyPDFLoader(url) # loading the pdf file using the PyPDFLoader class
doc = loader.load() # loading the document
 
# res = spliter.split_text(doc) # splitting the text into chunks of 100 characters with no overlap
# spliting the content of document 
doc_split = spliter.split_documents(doc) # splitting the document into chunks of 100 characters with no overlap

print(doc_split[0].page_content) # printing the result
print(len(doc_split)) # printing the number of chunks