from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
import uuid
from config import QDRANT_HOST, QDRANT_PORT


client = QdrantClient(
    host=QDRANT_HOST,
    port=QDRANT_PORT,
    https=False  # ✅ HTTP since port 6333 is not HTTPS-enabled
)

def init_collection(name):
    if name not in [c.name for c in client.get_collections().collections]:
        client.create_collection(name, vectors_config=VectorParams(size=384, distance=Distance.COSINE))

def store_vectors(name, texts, vectors):
    init_collection(name)
    points = [PointStruct(id=str(uuid.uuid4()), vector=v, payload={"text": t}) for t, v in zip(texts, vectors)]
    client.upsert(collection_name=name, points=points)

def retrieve_relevant_chunks(name, vector, k=3):
    result = client.search(collection_name=name, query_vector=vector, limit=k)
    return [hit.payload["text"] for hit in result]
