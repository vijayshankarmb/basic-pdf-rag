import ollama

response = ollama.embeddings(
    model = "nomic-embed-text",
    prompt = "radhe radhe"
)

embeddings = response['embedding']

print(len(embeddings))
print(embeddings[:5])
