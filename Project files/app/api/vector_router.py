from fastapi import APIRouter
from typing import List

router = APIRouter()

@router.get("/search-docs")
def search_docs(query: str):
    # Dummy example; replace with real search logic later
    results = [
        {"title": "Sustainability Report", "content": "Details about environment"},
        {"title": "Energy Saving", "content": "Use solar panels..."}
    ]
    return {"query": query, "results": results}