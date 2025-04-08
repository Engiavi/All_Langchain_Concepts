from langchain_google_genai import ChatGoogleGenerativeAI  #type: ignore
from langchain.prompts import PromptTemplate #type: ignore
from langchain_core.outputs import strOutputParser #type: ignore
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence #type: ignore

load_dotenv()