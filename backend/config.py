import os


# Use Railway internal host if deployed in same project
QDRANT_HOST = os.getenv("QDRANT_HOST", "qdrant.railway.internal")
QDRANT_PORT = int(os.getenv("QDRANT_PORT", 6333))