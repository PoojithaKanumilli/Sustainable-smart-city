from pinecone import Pinecone

pc = Pinecone(api_key="pcsk_4gxSkh_79DsRN7wdhpCawCezASeJ6jkZdnHBBM2bH2uZj5UnK8f18qQmvbDXZRYRL27AZ4")
index_name = "smartcity"

if index_name not in [index["name"] for index in pc.list_indexes()]:
    pc.create_index(name=index_name, dimension=384)

index = pc.Index(index_name)

def upsert_to_pinecone(vector_id, vector, metadata):
    index.upsert([(vector_id, vector, metadata)])

def search_pinecone(query_vector, top_k=5):
    return index.query(vector=query_vector, top_k=top_k, include_metadata=True)