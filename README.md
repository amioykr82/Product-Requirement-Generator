📄 Product Requirement Generator
AI-Powered PDF to Product Requirement Generator with RAG Architecture

This project allows teams to automatically generate high-quality product testing and functional requirements by uploading specification documents (PDFs) and asking intelligent questions. It uses Generative AI, section-aware document chunking, and a vector database (Qdrant) to deliver structured responses — just like a product analyst would.

🚀 Features
📎 Upload product specification documents (PDF)

💬 Ask contextual questions about requirements

🧠 Powered by GPT-4 and Sentence-BERT embeddings

📚 Uses Retrieval-Augmented Generation (RAG) with Qdrant

🔍 Returns structured output with Title and Scope and Objective

🎯 Section-aware PDF chunking for better AI context

🌐 Clean and modern frontend UI (ChatGPT-style)

🐳 Docker-compatible and Kubernetes-ready

📁 Project Structure
php
Copy
Edit
Product-Requirement-Generator/
├── backend/                  # FastAPI app
│   ├── main.py               # FastAPI routes
│   ├── config.py             # Configuration loader
│   ├── requirements.txt      # Python dependencies
│   ├── services/             # Modular AI logic
│   │   ├── pdf_parser.py     # PDF section chunker
│   │   ├── embedder.py       # Sentence-BERT embeddings
│   │   ├── graph_rag.py      # Qdrant-based retrieval
│   │   └── generator.py      # OpenAI GPT-4 generation logic
│   └── .env                  # OpenAI API key
│
├── frontend/                 # React frontend
│   ├── src/                  # UI logic and styles
│   ├── public/
│   └── package.json
│
└── qdrant/                   # (Optional) Mount for Qdrant volume
🛠️ Installation Guide
1️⃣ Clone the repository
bash
Copy
Edit
git clone https://github.com/your-username/product-requirement-generator.git
cd product-requirement-generator
2️⃣ Start Vector DB (Qdrant)
Make sure Docker is installed.

bash
Copy
Edit
docker run -p 6333:6333 qdrant/qdrant
3️⃣ Backend Setup
bash
Copy
Edit
cd backend
python -m venv .venv
.venv\Scripts\activate           # On Windows
# source .venv/bin/activate     # On Mac/Linux

pip install -r requirements.txt
Create a .env file in backend/:

env
Copy
Edit
OPENAI_API_KEY=your_openai_api_key_here
Start the API server:

bash
Copy
Edit
uvicorn main:app --reload --port 8000
Visit backend docs: http://localhost:8000/docs

4️⃣ Frontend Setup
bash
Copy
Edit
cd ../frontend
npm install
npm start
Access UI at: http://localhost:3000

✅ How to Use
Upload a product spec PDF file

Enter a professional query, e.g.:

“Write a requirement for user authentication with OTP verification and password fallback”

Click Generate Requirement

Get AI-generated:

📌 Title (introductory explanation)

🎯 Scope and Objective (use case, boundaries, and value)

Review supporting source document chunks

🧠 Tech Stack
Layer	Tools/Libs
Frontend	React + Axios + CSS
Backend	FastAPI + OpenAI + Sentence-BERT
Vector DB	Qdrant (via Docker)
Embeddings	all-MiniLM-L6-v2 (sentence-transformers)
Generation	OpenAI GPT-4
Deployment	Docker-ready, Kubernetes supported

🧪 Sample Prompt
Write requirement for login authentication
✅ Output includes full definition and scope:

bash
Copy
Edit
📌 Title
The login authentication requirement ensures that only verified users gain access...

🎯 Scope and Objective
This requirement covers username/password login, multi-factor authentication, etc.
🐳 Optional: Dockerize the Backend
Create Dockerfile inside backend/:

dockerfile
Copy
Edit
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
💡 Future Improvements
PDF preview with page references

Chat history and export

PDF table parsing and validation

Admin panel to review generated requirements

🙌 Contribution
Feel free to fork and submit PRs. Let’s build the future of intelligent product development.

📄 License
MIT License – use freely and responsibly.