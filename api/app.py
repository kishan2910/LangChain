from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv 

load_dotenv()
# os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]="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"
# LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
# LANGCHAIN_PROJECT = "Custom_Chatbot"

app=FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API Server"
    )

llm=Ollama(model="llama3")

prompt=ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words.")

add_routes(
    app,
    prompt|llm,
    path="/essay"
)

if __name__=="__main__":
    uvicorn.run(app, host="localhost", port=8000)