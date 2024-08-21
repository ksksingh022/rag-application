import os
import streamlit as st
from openai import AzureOpenAI
from dotenv import load_dotenv

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

while(True):
    prompt = input("Enter your query:")
    messages = [{
        'role':'user','content':prompt
    },]
    response = client.chat.completions.create(messages=messages,model='gpt-35-turbo')
    print(response.choices[0].message.content);
