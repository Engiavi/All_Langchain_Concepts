from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up the embeddings model
embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

# Create some sample documents
docs = [
    Document(page_content="Virat kohli is a batter", metadata={"source": "doc1"}),
    Document(page_content="Ravindra jadeja is a all rounder", metadata={"source": "doc2"}),
    Document(page_content="Jasprit bumrah is a bowler", metadata={"source": "doc3"}),
]

# Create Chroma vector store and persist the documents
vector_stores = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    persist_directory="my_chroma_db",
    collection_name="sample"
)
# add the documents to the vector store
vector_stores.add_documents(docs)
# getting the vector store(from chroma db)
see_vector = vector_stores.get(include=['embeddings', 'documents', 'metadatas'])

# print the vector store
print(see_vector)
print("Documents added to Chroma vector store.")# basic print statement

# getting the relevant query using similarity search
print(vector_stores.similarity_search( 
    query="Who among is bowler",
    k=1,# returns the k most similar documents
))
# getting the relevant query using similarity search with score(value should so small,means it lie nearby the query)
print(vector_stores.similarity_search_with_score( 
    query="Who among is bowler",
    k=1,# returns the k most similar documents
))

#  similarity_search_with_score is used to get the score of the similarity search with output
#  similarity_search is used to get the most similar documents without similarity score
# we can apply filter in meta-data
# print(vector_stores.similarity_search_with_score(
#     query="",
#     k=1,# returns the k most similar documents
#     filter={"source": "doc2"}
# ))

# creating the update document object
updated_docs = Document(page_content="Ravindra jadeja is a all rounder and he is spinner", metadata={"source": "doc2"})

# update the document in the vector store
vector_stores.update_document(
    document_id = 'd5d2eb43-dab1-45ed-8479-c4cea3b652d2',
    document=updated_docs
)
# again query the updated part
print(vector_stores.similarity_search_with_score(
    query="who is the spinner",
    k=1, 
))

print("*********************")
# delete the document from the vector store
vector_stores.delete(ids = ['d5d2eb43-dab1-45ed-8479-c4cea3b652d2'])
# again query the updated part
print(vector_stores.similarity_search_with_score(
    query="who is the spinner",
    k=1, 
))