from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import tempfile
from services import pdf_parser, embedder, graph_rag, generator

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

COLLECTION = "product-reqs"

@app.post("/query")
async def query_pdf(file: UploadFile = File(...), query: str = Form(...)):
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    chunks = pdf_parser.extract_text_chunks(tmp_path)
    vectors = embedder.embed_texts(chunks)
    graph_rag.store_vectors(COLLECTION, chunks, vectors)

    query_vec = embedder.embed_texts([query])[0]
    top_chunks = graph_rag.retrieve_relevant_chunks(COLLECTION, query_vec)

    answer = generator.generate_answer("\n\n".join(top_chunks), query)
    return {"answer": answer, "used_chunks": top_chunks}
