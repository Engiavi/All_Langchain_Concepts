from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env

embedding = OpenAIEmbeddings(model="text-embeddings-3-small",dimensions=32)
result = embedding.embed_query("What is the capital of India?")

print(str(result)) 