import os
import zipfile
from PyPDF2 import PdfReader
from constants import EXTRACT_TO


def extractZip(zipPath):
    extractTo = EXTRACT_TO
    os.makedirs(extractTo,exist_ok=True)

    with zipfile.ZipFile(zipPath, 'r') as zip_ref:
        zip_ref.extractall(extractTo)

def readFromPDF(pdfPath):
    text = ""
    with open(pdfPath,"rb") as file:
        reader = PdfReader(file)
        for pageNum in range(len(reader.pages)):
            page = reader.pages[pageNum]
            text += page.extract_text()
    return {"content":text}

def readFromText(textPath):
    with open(textPath,'r') as file:
        text = file.read()
    return {"content":text}

def extractTextFromFiles(filepath,filetype):
    print(filetype)
    if(filetype==".pdf"):
        data = readFromPDF(filepath)
        return data
    else: return {"content":"error occured!!"} 
