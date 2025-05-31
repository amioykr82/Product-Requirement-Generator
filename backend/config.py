import os

# Use internal DNS of Qdrant in Railway private networking
QDRANT_HOST = os.getenv("QDRANT_HOST", "qdrant.railway.internal")
QDRANT_PORT = int(os.getenv("QDRANT_PORT", 6333))
