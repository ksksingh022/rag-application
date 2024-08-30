from config import UPLOAD_TO
import os
from utils import extractTextFromFiles
from langchain.text_splitter import RecursiveCharacterTextSplitter

def recursiveCharacterTS():
    uploadedFilePath = UPLOAD_TO+'sample.pdf'

    _,filetype = os.path.splitext(uploadedFilePath)
    text_data = extractTextFromFiles(uploadedFilePath,filetype)['content']

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 256,
        chunk_overlap  = 20
    )

    chunks = text_splitter.create_documents([text_data])
    return chunks
    # print(chunks)