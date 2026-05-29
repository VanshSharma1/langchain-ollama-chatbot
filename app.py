from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"]="true"
prompt=ChatPromptTemplate.from_messages([
    (
        "system",
        "You are helpful AI assistant answer user question clearly"
    ),
    (
        "user",
        "question:{question}"
    )
])
st.title("Langchain + OpenAI Demo")
input_text=st.text_input("Enter your question here ")
llm = ChatOllama(model="gemma3:1b")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser
if input_text:
    response=chain.invoke(
        {
            "question":input_text
        }
    )
    st.write(response)
