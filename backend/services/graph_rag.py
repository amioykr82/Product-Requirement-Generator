from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
import uuid
from config import QDRANT_HOST, QDRANT_PORT

# Connect to Qdrant via Railway internal networking
client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)

def init_collection(name):
    collections = client.get_collections().collections
    if name not in [c.name for c in collections]:
        client.create_collection(
            collection_name=name,
            vectors_config=VectorParams(size=384, distance=Distance.COSINE)
        )

def store_vectors(name, texts, vectors):
    init_collection(name)
    points = [
        PointStruct(id=str(uuid.uuid4()), vector=vector, payload={"text": text})
        for text, vector in zip(texts, vectors)
    ]
    client.upsert(collection_name=name, points=points)

def retrieve_relevant_chunks(name, vector, k=3):
    results = client.search(collection_name=name, query_vector=vector, limit=k)
    return [hit.payload["text"] for hit in results]
