from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env

embedding = OpenAIEmbeddings(model="text-embeddings-3-small",dimensions=32)
documents = [
    "What is the capital of India?",
    "What is the capital of France?",
    "What is the capital of Germany?",
    "What is the capital of Italy?",
    "What is the capital of Japan?",
    "What is the capital of China?",
    "What is the capital of Russia?",
    "What is the capital of Australia?",
    "What is the capital of Brazil?",
    "What is the capital of Canada?"
]
result = embedding.embed_documents(documents)

print(str(result)) 