from langchain_community.retrievers import WikipediaRetriever

retriever = WikipediaRetriever(
    top_k_results = 2,
    lang = "en",
)

query = "what is human soul"

docs = retriever.invoke(query) # here we use invoke because it is a runnable.
print(docs)
for i, doc in enumerate(docs):
    print(f"Document {i+1}:")
    print(f"Content: {doc.page_content}..")