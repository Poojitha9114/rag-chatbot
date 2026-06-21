from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pickle
import os

vectorizer = TfidfVectorizer()
chunks_store = []

def get_embeddings(chunks):
    global vectorizer, chunks_store
    chunks_store = chunks
    matrix = vectorizer.fit_transform(chunks)
    return matrix.toarray()

def search_chunks(query, chunks, top_k=2):
    global vectorizer
    if not chunks_store:
        vectorizer.fit(chunks)
    query_vec = vectorizer.transform([query])
    chunk_matrix = vectorizer.transform(chunks)
    scores = cosine_similarity(query_vec, chunk_matrix)[0]
    top_indices = np.argsort(scores)[::-1][:top_k]
    return [chunks[i] for i in top_indices]

if __name__ == "__main__":
    test_chunks = ["Python developer with FastAPI skills", 
                   "Data science and machine learning",
                   "SQL database management"]
    embeddings = get_embeddings(test_chunks)
    print(f"Embeddings shape: {embeddings.shape}")
    results = search_chunks("python web development", test_chunks)
    print(f"Search result: {results[0][:100]}")
    print("Working!")