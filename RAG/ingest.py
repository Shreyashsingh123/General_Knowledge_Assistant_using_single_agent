import os
from sentence_transformers import SentenceTransformer
from pathlib import Path
import chromadb

BASE_DIR=Path(__file__).resolve().parent.parent
Data_folder=BASE_DIR/"Data"
DB_Path=BASE_DIR/"vectordb"

client=chromadb.PersistentClient(path=DB_Path)

embedding=SentenceTransformer("all-MiniLM-L6-v2")
try:
    client.delete_collection(name="GK_KB")
except:
    pass

collection=client.get_or_create_collection(name="GK_KB")

def chunk_text(text,chunk_size=300):
    chunks=[]
    for i in range(0,len(text),chunk_size):
        chunks.append(text[i:i+chunk_size])
        
    return chunks
id=0
for root,_,files in os.walk(Data_folder):
    for file in files:
        if not file.endswith(".txt"):
            continue
        file_path=os.path.join(root,file)
        with open(file_path,"r",encoding="utf-8") as f:
            text=f.read()

        chunk=chunk_text(text)
        for chun in chunk:
            embeddings=embedding.encode(chun).tolist()
            collection.add(
                ids=[str(id)],
                documents=[chun],
                embeddings=embeddings,
                metadatas=[{
                    'subject':os.path.basename('root'),
                    'file':file
                }]
            )
            id+=1

print(id)
        

