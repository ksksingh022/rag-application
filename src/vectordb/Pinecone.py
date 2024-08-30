from config import PINECONE_API_KEY
# from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
# import time

# pc = Pinecone(api_key=PINECONE_API_KEY)

# index_name="pc_vector_"+str(int(time.time))
# pc.create_index(
#     name=index_name,
#     dimension=1536,
#     metric="cosine",
#     spec=ServerlessSpec(cloud="aws", region="us-east-1"),
# )
# while not pc.describe_index(index_name).status["ready"]:
#     time.sleep(1)

# index = pc.Index(index_name)

index_name = "testing_rag"

def addDocsToVectorDB(docs,embeddings):
    pineconeDB = PineconeVectorStore.from_documents(
        docs,
        index_name = index_name,
        embedding = embeddings
    )