from langchain_huggingface import HuggingFaceEmbeddings
 
  # Load environment variables from .env

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

text = "What is the capital of India?"

result = embedding.embed_query(text)
print(str(result))
 