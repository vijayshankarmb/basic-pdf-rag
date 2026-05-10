import ollama
from pdf_reader import extract_text
from chunker import split_into_chunks
from embedder import generate_embeddings
from vector_storage import store_in_chromadb, query_chromadb

def generate_llm_answer(query):
    text = extract_text('data/sample.pdf')
    chunks = split_into_chunks(text)
    embeddings = generate_embeddings(chunks)
    collection = store_in_chromadb(chunks, embeddings)

    query_embedding = ollama.embeddings(model="nomic-embed-text", prompt=query)["embedding"]

    context = query_chromadb(collection, query_embedding, 3)

    prompt = f"Based on the context:{context}, answer the question: {query}, if the answer is not in the context, say 'I dont know', do not use any external knowledge, give answer in bullet points if possible, keep your response short, do not use emojis"

    response = ollama.chat(model="qwen2.5:3b", messages=[
        {
            "role": "user",
            "content": prompt
        }
    ])
    return response['message']['content']

result = generate_llm_answer("what is frontend")
print(result)


