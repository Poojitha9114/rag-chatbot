# 🤖 RAG Document Chatbot

A Retrieval-Augmented Generation (RAG) based document question-answering application that allows users to upload PDF documents and ask questions about their content using natural language.

The application extracts text from uploaded PDFs, divides the content into smaller chunks, creates embeddings, retrieves the most relevant chunks for a user's question, and uses the Google Gemini API to generate a context-based answer.

## 🚀 Live Demo

[Try the RAG Document Chatbot](https://rag-chatbot-bz6bcchrwybw9zuqxtj6v4.streamlit.app/)

## ✨ Features

- 📄 Upload PDF documents
- 📖 Extract text from PDF files
- ✂️ Split extracted text into smaller chunks
- 🔢 Generate embeddings for document chunks
- 🔎 Retrieve relevant document content using similarity search
- 🧠 Generate answers using Google Gemini
- 💬 Interactive chat interface built with Streamlit
- 📝 Maintain conversation history during a session
- 📚 Supports different types of PDF documents
- 🚫 Avoid generating answers when the requested information is not available in the document
- ☁️ Deployed on Streamlit Community Cloud

## 🛠️ Technologies Used

- Python
- Streamlit
- Google Gemini API
- Retrieval-Augmented Generation (RAG)
- Embeddings
- PyMuPDF
- scikit-learn
- python-dotenv

## 🏗️ Application Workflow

```text
                PDF Upload
                    │
                    ▼
             Extract PDF Text
                    │
                    ▼
              Text Chunking
                    │
                    ▼
          Generate Embeddings
                    │
                    ▼
             Store Embeddings
                    │
                    ▼
            User asks a question
                    │
                    ▼
          Similarity Search
                    │
                    ▼
          Retrieve Relevant Chunks
                    │
                    ▼
          Build Context + Question
                    │
                    ▼
             Google Gemini
                    │
                    ▼
             Generate Answer
                    │
                    ▼
          Display in Streamlit
🔄 How It Works
1. Upload a PDF

The user uploads a PDF document through the Streamlit interface.

2. Extract Text

The application extracts readable text from the uploaded PDF.

3. Chunk the Text

The extracted text is divided into smaller chunks so that relevant sections can be retrieved efficiently.

4. Generate Embeddings

The document chunks are converted into numerical vector representations called embeddings.

5. Retrieve Relevant Content

When a user asks a question, the application searches the document chunks and retrieves the content most relevant to the question.

6. Generate the Answer

The retrieved content is provided to Google Gemini along with the user's question.

The model is instructed to answer using the provided document context.

7. Display the Result

The generated answer is displayed in the Streamlit chat interface.

💬 Example Questions

After uploading a PDF, users can ask questions such as:

What is the main topic of this document?
What are the key points?
Explain the main idea in simple terms.
What are the important concepts discussed?
What are the advantages mentioned?
What problems or challenges are described?
What are the key findings?
Summarize this section.
Explain this concept from the document.
What conclusion does the document provide?

The chatbot can be used with different types of PDF documents rather than being limited to a specific document type.

📚 Example Documents

The application can be used with documents such as:

Study materials
Research papers
Technical documentation
Project documentation
User manuals
Business reports
Books and articles
Course materials
Specifications and design documents
Other text-based PDF documents
📁 Project Structure
rag-chatbot/
│
├── app.py
├── chunker.py
├── embedder.py
├── gemini_chat.py
├── pdf_reader.py
├── vector_store.py
├── requirements.txt
├── .gitignore
└── README.md
⚙️ Run Locally
Prerequisites
Python 3.11 or later
Google Gemini API key
Git
1. Clone the repository
git clone https://github.com/Poojitha9114/rag-chatbot.git
cd rag-chatbot
2. Create a virtual environment
python -m venv venv
3. Activate the environment

Windows:

venv\Scripts\activate
4. Install dependencies
pip install -r requirements.txt
5. Configure the Gemini API key

Create a .env file in the project directory:

GEMINI_API_KEY=your_api_key_here

Do not upload your .env file or expose your API key publicly.

6. Run the application
streamlit run app.py

The application will open in your browser at:

http://localhost:8501
🔐 Environment Variables

The application uses the following environment variable:

GEMINI_API_KEY

The API key should be stored securely using environment variables.

For local development, it can be stored in a .env file.

For cloud deployment, configure it using the deployment platform's secrets or environment-variable settings.

☁️ Deployment

The application is deployed using Streamlit Community Cloud.

Live Application

Open the deployed application

The deployed application allows users to open the chatbot directly in a browser, upload a PDF, and interact with the document.

🎯 Use Cases

RAG-based document question answering can be useful for:

Document search
Research assistance
Study and learning
Technical documentation
Project documentation
Report analysis
Knowledge-base question answering
Information retrieval from large documents
🧠 RAG Concept

Retrieval-Augmented Generation combines information retrieval with a generative language model.

Instead of asking the language model to answer using only its general knowledge, the application first retrieves relevant information from the uploaded document and provides that information as context.

This helps the chatbot generate answers that are more closely grounded in the uploaded document.

User Question
      ↓
Retrieve Relevant Information
      ↓
Provide Retrieved Context to LLM
      ↓
Generate Context-Based Answer
⚠️ Limitations
The application works with text that can be extracted from PDFs.
Scanned or image-only PDFs may require OCR for reliable text extraction.
The quality of answers depends on the quality of the extracted text and retrieved chunks.
Gemini API availability and usage limits may affect responses.
Very large documents may require additional optimization for efficient retrieval.
🔒 Security

API keys should never be committed to the GitHub repository.

Make sure .env is included in .gitignore:

.env
venv/
__pycache__/
👩‍💻 Author

Poojitha Yeddula

GitHub:
https://github.com/Poojitha9114



Then your GitHub repository will have a proper README and your **Live Demo** link will be clickable.
