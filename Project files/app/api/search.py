# app/api/search.py
from fastapi import APIRouter, Query
from app.services.document_embedder import embed_text
from app.services.pinecone_index import search_pinecone

router = APIRouter()

@router.get("/search-docs")
async def search_docs(query: str = Query(...)):
    query_vector = embed_text(query)
    results = search_pinecone(query_vector)
    return {"results": results["matches"]}