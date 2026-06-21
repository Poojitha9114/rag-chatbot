from pdf_reader import extract_text
from chunker import split_into_chunks
from embedder import get_embeddings, search_chunks

all_chunks = []

def create_vector_store(pdf_path):
    global all_chunks
    print("Extracting text...")
    text = extract_text(pdf_path)
    all_chunks = split_into_chunks(text)
    print(f"Created {len(all_chunks)} chunks")
    get_embeddings(all_chunks)
    print(f"Stored {len(all_chunks)} chunks")
    return all_chunks

def search(query, top_k=2):
    return search_chunks(query, all_chunks, top_k)

if __name__ == "__main__":
    create_vector_store("test.pdf")
    print("\nTesting search...")
    results = search("What are the technical skills?")
    print(f"Found {len(results)} chunks")
    print(f"Preview: {results[0][:200]}")