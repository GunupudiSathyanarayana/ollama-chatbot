from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv(override=True)

## LangSmith tracking
os.environ["LANGSMITH_TRACING"]="true"
os.environ["LANGSMITH_API_KEY"]=os.getenv("LANGSMITH_API_KEY")
os.environ["LANGSMITH_ENDPOINT"]=os.getenv("LANGSMITH_ENDPOINT")
os.environ["LANGSMITH_PROJECT"]=os.getenv("LANGSMITH_PROJECT")

## Prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user queries"),
    ("user","Question: {question}")
])


## Build web application using Streamlit framework
## LLAMA2 is running on the local machine.
st.title("Chatbot Using LLAMA2 API")
input_text = st.text_input("Enter your prompt here:")

## Configure the Ollama LLM client to use the llama2 model
## By default, OllamaLLM connects to the local server (http://localhost:11434).
## Specify base_url to connect to a remote Ollama server.
llm = OllamaLLM(model="llama2") 
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

## Call the Ollama API when the user submits a question
if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)