from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv
load_dotenv()
documents = [
    Document(page_content = "langchain allows developers to build applications with LLMs"),
    Document(page_content = "Chroma is a vector database optimised for LLMs-based skills"),
    Document(page_content = "Embeddings convert text into high dimensional vectors"),
    Document(page_content = "OpenAI provide large number of embedding models"),
]

embedding  = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

vector_stores = Chroma.from_documents( # create a vector store from documents
    documents = documents,
    embedding = embedding,
    persist_directory = "my_chroma_db",
    collection_name = "sample"
)
# convert vector store to retriever
retriever = vector_stores.as_retriever(
    search_kwargs = {
        "k": 2,
    }
)

q = "Write steps to master langchain?"
res = retriever.invoke(q)#runnable object retriever

for i, doc in enumerate(res): # enumerate is used to get the index and value of the document
    print(f"Document {i+1}:")
    print(f"Content: {doc.page_content}..")