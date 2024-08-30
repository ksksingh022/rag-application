import os
import streamlit as st
from chunking.RecursiveCharacterTS import recursiveCharacterTS
from embedding.OpenAIEmbeddings import getEmbeddingModel
from langchain_pinecone import PineconeVectorStore
from langchain_core.prompts import ChatPromptTemplate
from config import AZURE_OPENAI_CLIENT
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

docs = recursiveCharacterTS()
embeddings = getEmbeddingModel()
# vectordb = PineconeVectorStore.from_documents(docs,embedding = embeddings,index_name='pinecone-index')
vectordb = PineconeVectorStore.from_existing_index(index_name='pinecone-index',embedding = embeddings)
# result = vectordb.similarity_search("who are authors of Retrieval-Augmented Generation for Large Language Models: A Survey")
# print(result[0].page_content)
prompt = ChatPromptTemplate.from_template("""
Answer the following questions based on the provided context.
<context>{context}</context>
question: {input}
""")
document_chain = create_stuff_documents_chain(AZURE_OPENAI_CLIENT,prompt)

retriever = vectordb.as_retriever()
retrival_chain = create_retrieval_chain(retriever,document_chain)

response = retrival_chain.invoke({"input":"who are authors of Retrieval-Augmented Generation for Large Language Models: A Survey"})
print(response['answer'])
# while(True):
#     prompt = input("Enter your query:")
#     messages = [{
#         'role':'user','content':prompt
#     },]
#     response = AZURE_OPENAI_CLIENT.chat.completions.create(messages=messages,model='gpt-35-turbo')
#     print(response.choices[0].message.content);


#1. Add Embedding Model
#2. See Pinecone code and follow same.
#3. complete end to end rag and move to UI.