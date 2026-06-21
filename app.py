import asyncio
import sys
import os
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
st.markdown("---")

for msg in st.session_state.messages:
    css_class = "user-msg" if msg["role"] == "user" else "bot-msg"
    icon = "👤" if msg["role"] == "user" else "🤖"
    st.markdown(f"""
    <div class='chat-msg {css_class}'>
        <strong>{icon}</strong> {msg["content"]}
    </div>""", unsafe_allow_html=True)

question = st.chat_input("Ask a question about your document...")

if question:
    if not st.session_state.chunks:
        st.warning("Please upload a PDF first")
    else:
        st.session_state.messages.append({"role": "user", "content": question})
        
        relevant = search_chunks(question, st.session_state.chunks)
        context = "\n\n".join(relevant)
        
        prompt = f"""Answer based ONLY on this context:
{context}

Question: {question}
Answer:"""
        
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )
            answer = response.text
        except Exception as e:
            answer = f"API Error: {str(e)[:100]}. Please try again later."
        
        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.rerun()