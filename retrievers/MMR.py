# MMr stands as maximum marginal relevance, a method for document retrieval that balances relevance and diversity.
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv
load_dotenv()
documents = [
    Document(page_content = "langchain allows developers to build applications with LLMs"),
    Document(page_content = "Chroma is a vector database optimised for LLMs-based skills"),
    Document(page_content = "Embeddings convert text into high dimensional vectors"),
    Document(page_content = "OpenAI provide large number of embedding models"),
    Document(page_content = "MMR helps you to select the most relevant and diverse documents"),
    Document(page_content = "LLMs support various vector stores and databases such as pinecone, Chroma, FAISS and more"),
]

embedding  = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

vector_stores = FAISS.from_documents( # create a vector store from documents, using FAISS vector store
    documents = documents,
    embedding = embedding,
)

retriever  = vector_stores.as_retriever(
    search_type = "mmr", #search type is MMR, means we are using MMR for retrieval
    search_kwargs = {
        "k": 3, # number of documents to retrieve
        "lambda_mult": 0, # lambda multiplier for MMR, it controls the trade-off between relevance and diversity. This parameter controls the balance between maximizing diversity (closer to 0) and maximizing relevance (closer to 1) in the retrieved results. 
    }
)

query = "Write is langchain?"
res = retriever.invoke(query) # runnable object retriever
for i, doc in enumerate(res): # enumerate is used to get the index and value of the document
    print(f"Document {i+1}:")
    print(f"Content: {doc.page_content}..")
