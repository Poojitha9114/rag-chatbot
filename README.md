# 🤖 RAG Document Chatbot

A Retrieval-Augmented Generation (RAG) chatbot that answers questions from uploaded PDF documents using TF-IDF retrieval and Google Gemini.

## 🚀 Features

* Upload PDF documents
* Extract and chunk text
* TF-IDF based document search
* Context-aware answers using Gemini
* Chat history support
* Secure API key management with `.env`

## 🛠️ Tech Stack

* Python
* Streamlit
* Scikit-learn (TF-IDF)
* PyMuPDF
* Google Gemini API

## ▶️ Run Locally

```bash
git clone https://github.com/Poojitha9114/rag-chatbot.git
cd rag-chatbot

pip install -r requirements.txt
```

Create `.env`

```env
GEMINI_API_KEY=your_api_key
```

Run:

```bash
streamlit run app.py
```

## 📂 Project Structure

```text
rag-chatbot/
├── app.py
├── pdf_reader.py
├── chunker.py
├── embedder.py
├── vector_store.py
├── gemini_chat.py
└── README.md
```

## 💡 How It Works

PDF → Text Extraction → Chunking → TF-IDF Search → Gemini → Answer

## 🔒 Security

API keys are stored in `.env` and excluded from GitHub using `.gitignore`.
