import os
import uuid
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone, ServerlessSpec
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = os.getenv("PINECONE_ENV")  # e.g., "gcp-starter"
INDEX_NAME = os.getenv("INDEX_NAME")
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(INDEX_NAME)
model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_and_store_document(file_content, filename):
    lines = file_content.split('\n')
    chunks = [line for line in lines if line.strip() != ""]

    embeddings = model.encode(chunks).tolist()
    ids = [str(uuid.uuid4()) for _ in chunks]
    metadata = [{"text": chunk, "filename": filename} for chunk in chunks]
    to_upsert = list(zip(ids, embeddings, metadata))
    index.upsert(vectors=to_upsert)

    return {"message": f"Uploaded {len(chunks)} chunks from {filename}"}
