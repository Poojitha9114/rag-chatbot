def split_into_chunks(text, chunk_size=300, overlap=50):
    words = text.split()
    chunks = []
    start = 0
    
    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start = end - overlap
    
    return chunks

if __name__ == "__main__":
    sample = "word " * 1000
    chunks = split_into_chunks(sample)
    print(f"Total chunks: {len(chunks)}")
    print(f"First chunk word count: {len(chunks[0].split())}")
    print(f"Second chunk word count: {len(chunks[1].split())}")