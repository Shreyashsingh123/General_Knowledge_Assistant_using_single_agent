import os
from pathlib import Path
from sentence_transformers import SentenceTransformer
import chromadb

BASE_DIR=Path(__file__).resolve().parent.parent
Data_folder=BASE_DIR/"Data"
DB_Path=BASE_DIR/"vectordb"


client=chromadb.PersistentClient(path=DB_Path)
collection=client.get_or_create_collection(name="GK_KB")
embedding=SentenceTransformer("all-MiniLM-L6-v2")
def retreiver(query):
    embeddings=embedding.encode(query).tolist()
    result=collection.query(query_embeddings=embeddings,n_results=3)
    context="\n\n".join(result["documents"][0])
    print(context)

    return context