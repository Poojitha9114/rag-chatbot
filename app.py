import asyncio
import sys
import os
import time
from dotenv import load_dotenv
load_dotenv()
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import streamlit as st
from google import genai
from pdf_reader import extract_text
from chunker import split_into_chunks
from embedder import get_embeddings, search_chunks

st.set_page_config(page_title="RAG Document Chatbot", page_icon="🤖", layout="wide")

st.markdown("""
<style>
    .stApp { background: linear-gradient(135deg, #0f0c29, #302b63); }
    h1 { color: #a78bfa !important; }
    .chat-msg { background: rgba(255,255,255,0.05); border-radius: 10px; 
                padding: 12px; margin: 8px 0; color: white; }
    .user-msg { border-left: 3px solid #a78bfa; }
    .bot-msg { border-left: 3px solid #34d399; }
</style>
""", unsafe_allow_html=True)

st.title("🤖 RAG Document Chatbot")
st.markdown("Upload a PDF and ask questions about it")

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
client = genai.Client(api_key=GEMINI_API_KEY)

if "chunks" not in st.session_state:
    st.session_state.chunks = []
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar for PDF upload
with st.sidebar:
    st.header("📄 Upload Document")
    uploaded_file = st.file_uploader("Choose a PDF", type="pdf")
    
    if uploaded_file:
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.read())
        
        with st.spinner("Processing PDF..."):
            text = extract_text("temp.pdf")
            chunks = split_into_chunks(text)
            get_embeddings(chunks)
            st.session_state.chunks = chunks
        
        st.success(f"✅ Processed {len(chunks)} chunks")
        st.info(f"📝 Total characters: {len(text)}")


# Chat interface

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])


question = st.chat_input("Ask a question about your document...")


if question:

    if not st.session_state.chunks:
        st.warning("Please upload a PDF first")

    else:
        # Show user's question immediately
        st.session_state.messages.append({
            "role": "user",
            "content": question
        })

        with st.chat_message("user"):
            st.write(question)

        # Search relevant chunks
        relevant = search_chunks(
            question,
            st.session_state.chunks
        )

        context = "\n\n".join(relevant)

        prompt = f"""
You are a helpful assistant.

Answer the question ONLY using the provided context.

If the answer is not present in the context, say:
"I don't have that information."

Context:
{context}

Question:
{question}

Answer:
"""

        try:

            response = client.models.generate_content(
                model="gemini-3.5-flash",
                contents=prompt
            )

            answer = response.text

        except Exception as e:

            answer = f"API Error: {str(e)[:200]}"

        # Show answer immediately
        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })

        with st.chat_message("assistant"):
            st.write(answer)
