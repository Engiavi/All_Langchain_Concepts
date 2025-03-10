from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

st.header('Reasearch tool')
user_input = st.text_input("Enter your prompt")

if st.button("summarise"):
    result = model.invoke(user_input)
    st.write("Some random text:")  