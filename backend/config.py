import os

# Use internal DNS of Qdrant in Railway private networking
QDRANT_HOST = os.getenv("QDRANT_HOST", "qdrant-production-aac0.up.railway.app")
QDRANT_PORT = int(os.getenv("QDRANT_PORT", 6333))
