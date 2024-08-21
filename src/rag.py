import os
import streamlit as st
from openai import AzureOpenAI
from dotenv import load_dotenv
from constants import UPLOAD_TO
from utils import extractTextFromFiles
from langchain.text_splitter import RecursiveCharacterTextSplitter


load_dotenv()

openaiAPIKey = os.getenv("AZURE_OPENAI_API_KEY")
openaiAPIVersion = os.getenv("AZURE_OPENAI_API_VERSION")
openaiAPIBase = os.getenv("AZURE_OPENAI_API_BASE")
openaiAPIDeploymentName = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

client = AzureOpenAI(
    api_key=openaiAPIKey,
    api_version=openaiAPIVersion,
    base_url=f"{openaiAPIBase}/openai/deployments/{openaiAPIDeploymentName}",
)

uploadedFilePath = UPLOAD_TO+'sample.pdf'

_,filetype = os.path.splitext(uploadedFilePath)

text_data = extractTextFromFiles(uploadedFilePath,filetype)['content']


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 256,
    chunk_overlap  = 20
)

chunks = text_splitter.create_documents([text_data])

print(chunks)

while(True):
    prompt = input("Enter your query:")
    messages = [{
        'role':'user','content':prompt
    },]
    response = client.chat.completions.create(messages=messages,model='gpt-35-turbo')
    print(response.choices[0].message.content);
