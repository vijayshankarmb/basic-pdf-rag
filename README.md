# PDF-RAG API

A beginner-friendly RAG (Retrieval-Augmented Generation) backend project built using Python, FastAPI, Ollama, and ChromaDB.

This project allows users to upload PDFs and ask questions about the document using a local LLM.

---

# Features

- PDF upload API
- PDF text extraction
- Text chunking with overlap
- Embedding generation using Ollama
- Vector storage using ChromaDB
- Semantic search retrieval
- RAG-based answer generation
- FastAPI backend with Swagger UI

---

# Tech Stack

- Python
- FastAPI
- Ollama
- ChromaDB
- pypdf
- Uvicorn

---

# Project Structure

```bash
pdf-rag/
│
├── app/
│   ├── main.py
│   ├── routes/
│   └── services/
│
├── data/
├── db/
├── README.md
└── pyproject.toml
```

---

# How It Works

1. Upload PDF
2. Extract text from PDF
3. Split text into chunks
4. Generate embeddings
5. Store vectors in ChromaDB
6. Retrieve relevant chunks
7. Generate answer using Qwen LLM

---

# API Endpoints

## Upload PDF

```http
POST /upload-pdf
```

## Chat

```http
POST /chat
```

Request Body:

```json
{
  "query": "What is Python?"
}
```

---

# Installation

## Clone Repository

```bash
git clone <your-repo-url>
cd pdf-rag
```

## Create Virtual Environment

```bash
uv venv
```

Activate environment:

### Windows

```bash
.venv\Scripts\activate
```

### Linux/Mac

```bash
source .venv/bin/activate
```

## Install Dependencies

```bash
uv sync
```

---

# Install Ollama Models

```bash
ollama pull nomic-embed-text
ollama pull qwen2.5:3b
```

---

# Run Server

```bash
uvicorn app.main:app --reload
```

---

# Swagger Docs

Open:

```txt
http://127.0.0.1:8000/docs
```

---

# Future Improvements

- Multi-document support
- Better chunking
- LangChain integration
- AI agents
- Frontend UI
- Deployment

---

# Author

Vijay Shankar
```