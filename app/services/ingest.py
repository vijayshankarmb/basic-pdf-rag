
from services.pdf_reader import extract_text
from services.chunker import split_into_chunks
from services.embedder import generate_embeddings
from services.vector_storage import store_in_chromadb

def ingestion(pdf_path):
    text = extract_text(pdf_path)
    chunks = split_into_chunks(text)
    embeddings = generate_embeddings(chunks)
    collection = store_in_chromadb(chunks, embeddings)

    return collection



