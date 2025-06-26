# app/api/upload.py
from fastapi import APIRouter, UploadFile
from app.services.document_embedder import embed_text, generate_doc_id
from app.services.pinecone_index import upsert_to_pinecone

router = APIRouter()

@router.post("/upload-doc")
async def upload_doc(file: UploadFile):
    content = await file.read()
    content_str = content.decode("utf-8")
    
    vector = embed_text(content_str)
    doc_id = generate_doc_id()
    metadata = {"filename": file.filename, "text": content_str[:200]}  # store preview

    upsert_to_pinecone(doc_id, vector, metadata)
    return {"message": "Document uploaded successfully", "doc_id": doc_id}