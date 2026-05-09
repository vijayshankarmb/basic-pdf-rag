
import ollama

def chunks_into_embeddings(chunks):
    embedding = []
    for chunk in chunks:
        response = ollama.embeddings(
            model="nomic-embed-text",
            prompt=chunk
        )
        embedding.append(response['embedding'])
    return embedding

