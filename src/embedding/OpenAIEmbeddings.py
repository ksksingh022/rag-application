from langchain_openai import AzureOpenAIEmbeddings
from config import AZURE_OPENAI_API_BASE, AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT_NAME

def getEmbeddingModel():
    embeddings = AzureOpenAIEmbeddings(base_url=f"{AZURE_OPENAI_API_BASE}/openai/deployments/{AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT_NAME}")
    return embeddings