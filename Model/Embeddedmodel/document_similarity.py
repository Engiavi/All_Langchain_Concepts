from langchain_output import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model ="text-embedding-3-small",dimensions=300)

documents = [
     "Sachin Tendulkar, known as the 'God of Cricket,' is the highest run-scorer in international cricket history.",
    "Virat Kohli, with his aggressive captaincy and consistent batting, has established himself as one of the modern greats.",
    "MS Dhoni, India's most successful captain, led the team to victory in the 2007 T20 World Cup, 2011 ODI World Cup, and 2013 Champions Trophy.",
    "Kapil Dev's all-round brilliance helped India secure its first-ever World Cup victory in 1983.",
    "Rohit Sharma holds the record for the highest individual score in an ODI, scoring 264 runs against Sri Lanka.",
    "Anil Kumble, one of India's greatest spinners, took all 10 wickets in a Test innings against Pakistan in 1999.",
    "Sunil Gavaskar was the first batsman to score 10,000 runs in Test cricket.",
    "Rahul Dravid, 'The Wall' of Indian cricket, was known for his impeccable technique and patience at the crease.",
    "Yuvraj Singh's six sixes in an over against England in the 2007 T20 World Cup remains an iconic moment in cricket history.",
    "Jasprit Bumrah's unique bowling action and lethal yorkers have made him one of the best fast bowlers in the world."
]
query = 'tell me about virat kohli'

doc_embeddings = embedding.embed_documents(documents)
query_embeddings = embedding.embed_query(query)

scores = cosine_similarity([query_embeddings],doc_embeddings)[0]

index,score = sorted(list(enumerate(scores)),key = lambda x:x[1])[-1]

print(query)
print(documents[index])
print("similarity score is: ",score)

