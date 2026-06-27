import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv

load_dotenv()

def get_openai_response(query):
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.5, openai_api_key=os.getenv("OPENAI_API_KEY"))
    response = llm([HumanMessage(content=query)])
    return response.content

st.set_page_config(page_title="LangChain ChatBot", page_icon="🤖", layout="wide")
st.header("LangChain ChatBot")

input = st.text_input("Enter your query here", key="input")
submit = st.button("Submit")

if submit and input:
    response = get_openai_response(input)
    st.write(response)
