import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
import getpass

load_dotenv()

def prompt_and_set_env_var(var_name, prompt_message):
    if not os.getenv(var_name):
        os.environ[var_name] = getpass.getpass(prompt_message)
    return os.getenv(var_name)

AZURE_OPENAI_API_KEY = prompt_and_set_env_var("AZURE_OPENAI_API_KEY", "Enter your Azure OpenAI API key: ")
AZURE_OPENAI_API_VERSION = prompt_and_set_env_var("AZURE_OPENAI_API_VERSION", "Enter your Azure OpenAI Version: ")
AZURE_OPENAI_API_BASE = prompt_and_set_env_var("AZURE_OPENAI_API_BASE", "Enter your Azure OpenAI API Base: ")
AZURE_OPENAI_DEPLOYMENT_NAME = prompt_and_set_env_var("AZURE_OPENAI_DEPLOYMENT_NAME", "Enter your Azure OpenAI Deployment Name: ")
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT_NAME = prompt_and_set_env_var("AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT_NAME","Enter your Azure OpenAI Deployment Name: ")
AZURE_OPENAI_CLIENT = AzureChatOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    api_version=AZURE_OPENAI_API_VERSION,
    base_url=f"{AZURE_OPENAI_API_BASE}/openai/deployments/{AZURE_OPENAI_DEPLOYMENT_NAME}",
)

PINECONE_API_KEY = prompt_and_set_env_var("PINECONE_API_KEY","Enter your Azure OpenAI API key: ")

EXTRACT_TO = "./../extracted-docs/"
UPLOAD_TO = "./../uploaded-files/"

