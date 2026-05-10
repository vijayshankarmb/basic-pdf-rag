import ollama
from services.pdf_reader import extract_text
from services.chunker import split_into_chunks
from services.embedder import generate_embeddings
from services.vector_storage import store_in_chromadb, query_chromadb

text = extract_text('data/sample.pdf')
chunks = split_into_chunks(text)
embeddings = generate_embeddings(chunks)
collection = store_in_chromadb(chunks, embeddings)

query = "what is frontend?"
query_embedding = ollama.embeddings(model="nomic-embed-text", prompt=query)["embedding"]

result = query_chromadb(collection, query_embedding, 3)
print(query)
print(result)

