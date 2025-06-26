import os
from dotenv import load_dotenv
from pinecone import Pinecone
load_dotenv()
pc = Pinecone(api_key=os.getenv("pcsk_6EWDKR_BuNKdURjUAkfMMLtXB9oGWuz2mvGCXSxRMJDE7XDEqE4ETJ7F91BJxA8yuKeKot"))
index_name = os.getenv("smart")
if index_name not in pc.list_indexes().names():
    pc.create_index(name=index_name, dimension=1024, metric="cosine")
    print(f"Created index: {index_name}")
else:
    print(f"Using existing index: {index_name}")
index = pc.Index(index_name)

sample_data = {
    "id": "example-id",
    "values": [0.1] * 1024   
}
index.upsert(vectors=[sample_data])
print("Upsert complete.")
