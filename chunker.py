def chunk_text(text,chunk_size = 100,overlap = 20):
    words = text.split()
    chunks = []
    i = 0 
    while i < len(words):
        chunk = words[i:i + chunk_size]
        chunks.append(" ".join(chunk))
        i += chunk_size - overlap
    return chunks

if __name__ == "__main__":
    sample = "words " * 50 
    chunks = chunk_text(sample, chunk_size=20,overlap=5)
    for i,chunk in enumerate(chunks):
        print(f"chunk {i+1}: {chunk[:30]}...")