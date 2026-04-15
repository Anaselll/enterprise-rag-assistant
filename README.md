# 🔍 RAG System

A minimal **Retrieval-Augmented Generation** pipeline built with LangChain, FAISS, and FastAPI.

> Simulates an enterprise knowledge base using [`data/entreprise.pdf`](./data/entreprise.pdf) as the document source.

---

##  Features

-  PDF ingestion & chunking
-  Sentence-transformer embeddings
-  FAISS vector store for fast similarity search
-  LLM-powered answers via Groq
-  REST API with FastAPI

---

## 🗂 Project Structure

```
rag_project/
├── app/
│   ├── api/          # FastAPI routes
│   ├── core/         # Config & settings
│   ├── models/       # Request/response schemas
│   ├── rag/          # RAG pipeline (loader, chunker, embeddings, vector store, engine)
│   └── main.py
├── data/
│   └── entreprise.pdf  # Simulated enterprise document
└── docker/
```

---

##  Getting Started

```bash
# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env  # then fill in your API keys

# Run the API
uvicorn app.main:app 
```

---

## 🛠 Stack

| Layer | Tool |
|---|---|
| LLM | Groq (`langchain-groq`) |
| Embeddings | HuggingFace Sentence Transformers |
| Vector Store | FAISS |
| Framework | FastAPI + LangChain |
| PDF Parsing | PyPDF |

---

## 📄 License

MIT
