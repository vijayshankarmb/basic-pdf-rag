
from pdf_reader import extract_text
from chunker import split_into_chunks
from embedder import generate_embeddings
from vector_storage import store_in_chromadb

def ingestion():
    text = extract_text('data/sample.pdf')
    chunks = split_into_chunks(text)
    embeddings = generate_embeddings(chunks)
    collection = store_in_chromadb(chunks, embeddings)

    return collection

