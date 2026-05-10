import chromadb

client = chromadb.PersistentClient(path="db")

collection = client.get_or_create_collection(name="pdf-chunks")

def store_in_chromadb(chunks, embeddings):
    collection.add(
        ids = [str(i) for i in range(len(chunks))],
        documents=chunks,
        embeddings=embeddings
    )
    return collection

def query_chromadb(query_embedding, n_results):
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )
    return results['documents'][0]



