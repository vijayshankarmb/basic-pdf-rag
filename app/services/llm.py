import ollama
from services.vector_storage import query_chromadb

def generate_llm_answer(query):

    query_embedding = ollama.embeddings(model="nomic-embed-text", prompt=query)["embedding"]

    context = query_chromadb(query_embedding, 3)

    prompt = f"Based on the context:{context}, answer the question: {query}, if the answer is not in the context, say 'I dont know', do not use any external knowledge, give answer in bullet points if possible, keep your response short, do not use emojis"

    response = ollama.chat(model="qwen2.5:3b", messages=[
        {
            "role": "user",
            "content": prompt
        }
    ])
    return response['message']['content']




