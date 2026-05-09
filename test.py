from services.pdf_reader import extract_text
from services.chunker import split_into_chunks
from services.embedder import chunks_into_embeddings

text = extract_text('data/sample.pdf')
chunks = split_into_chunks(text)
embeddings = chunks_into_embeddings(chunks)
print("embeddings: ",len(embeddings))
print("chunks: ", len(chunks))
print(len(embeddings[0]))

