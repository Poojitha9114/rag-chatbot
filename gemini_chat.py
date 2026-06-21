from google import genai
from vector_store import create_vector_store, search
from dotenv import load_dotenv
load_dotenv()
import os

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
client = genai.Client(api_key=GEMINI_API_KEY)

def ask_question(question, chunks):
    relevant_chunks = search(question)
    context = "\n\n".join(relevant_chunks)
    
    prompt = f"""You are a helpful assistant. Answer the question based ONLY on the context below.
If the answer is not in the context, say "I don't have that information."

Context:
{context}

Question: {question}

Answer:"""
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return response.text

if __name__ == "__main__":
    chunks = create_vector_store("test.pdf")
    print("Chatbot ready!")
    print()
    
    questions = [
        "What projects has this person built?",
        "What programming languages does this person know?",
        "What is the person's email address?"
    ]
    
    for q in questions:
        print(f"Q: {q}")
        print(f"A: {ask_question(q, chunks)}")
        print("-" * 50)