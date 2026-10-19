# 🎥 RAG-Based AI Video Assistant

An AI-powered video assistant built using Python, Large Language Models (LLMs), and Retrieval-Augmented Generation (RAG). This project extracts text from video content, processes it into searchable chunks, and helps users find relevant information by asking questions about the video.

## 🚀 Features

- 🎬 **Video Transcription:** Extracts text from video audio.
- ✂️ **Text Chunking:** Splits transcripts into smaller, manageable chunks.
- 🔢 **Embeddings:** Converts text into numerical representations for semantic search.
- 🔍 **Information Retrieval:** Retrieves relevant transcript content based on user queries.
- 🤖 **AI-Powered Answers:** Uses an LLM to generate answers from retrieved context.
- 📚 **RAG Architecture:** Combines information retrieval with language generation.

## 🛠️ Technologies Used

- Python
- Large Language Models (LLMs)
- Retrieval-Augmented Generation (RAG)
- Text Embeddings
- Vector Search
- FFmpeg
- Streamlit (if used in the application)

## 📂 Project Structure

```text
RAG-Based-AI-Video-Assistant/
├── app.py
├── llm.py
├── video_to_text.py
├── requirements.txt
├── rag/
│   ├── chunking.py
│   ├── embeddings.py
│   ├── retrieval.py
│   └── vector_store.py
└── transcripts/
```

## ⚙️ Installation

**1. Clone the repository**

```bash
git clone https://github.com/sundarampd88/RAG-Based-AI-Video-Assistant.git
cd RAG-Based-AI-Video-Assistant
```

**2. Create a virtual environment**

```bash
python -m venv venv
```

**3. Activate the environment**

Windows Git Bash:

```bash
source venv/Scripts/activate
```

**4. Install dependencies**

```bash
pip install -r requirements.txt
```

**5. Configure environment variables**

Create a `.env` file and add the API key or other settings required by your configured LLM provider. Never upload API keys or secrets to GitHub.

## ▶️ Usage

Run the application using the entry point configured in the project. For example, if `app.py` uses Streamlit:

```bash
streamlit run app.py
```

Follow the application interface to process video content and ask questions about the transcript.

## 🧠 How It Works

1. Upload or provide video content.
2. Extract the audio transcript.
3. Split the transcript into text chunks.
4. Generate embeddings for the chunks.
5. Retrieve the most relevant chunks for a user's question.
6. Pass the retrieved context to the LLM.
7. Generate an answer grounded in the video transcript.

## 🎯 Project Goal

The goal of this project is to demonstrate how Generative AI, semantic search, and Retrieval-Augmented Generation can be combined to build a practical question-answering system for video content.

## 👨‍💻 Author

**Sundaram PD Tiwari**

GitHub: [@sundarampd88](https://github.com/sundarampd88)

---

⭐ If you find this project interesting, consider giving it a star!
