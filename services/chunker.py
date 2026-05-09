from pdf_reader import extract_text

def split_init_chunks(text, chunnk_size=500, overlap=50):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunnk_size
        chunk = text[start:end]
        chunks.append(chunk)

        start = end - overlap
    return chunks


