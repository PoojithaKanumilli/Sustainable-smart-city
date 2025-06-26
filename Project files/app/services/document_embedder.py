# app/services/document_embedder.py
from sentence_transformers import SentenceTransformer
import uuid

model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_text(content: str):
    return model.encode(content).tolist()

def generate_doc_id():
    return str(uuid.uuid4())