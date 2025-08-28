# AI Microservices API with LangChain & FastAPI

This project provides a robust backend for three distinct AI services, exposed as a REST API using FastAPI and powered by LangChain. It leverages local, open-source LLMs through Ollama to ensure privacy and control.

## Features

-   **📝 `/summarize`**: An endpoint that accepts a block of text and returns a concise summary.
-   **❓ `/qa`**: A Retrieval-Augmented Generation (RAG) endpoint that answers questions based on a local knowledge base (`data/document.txt`).
-   **🗺️ `/learn-path`**: A personalized coaching endpoint that suggests a learning roadmap based on a user's profile and goals.

## Project Structure

The project is organized for clarity and modularity, separating API logic from the AI chain definitions.

```
.
├── .env                  # Environment variables (model names)
├── .gitignore            # Files to ignore for Git
├── README.md             # This file
├── data                  # Folder for documents used by the RAG agent
├── frontend.py           # The Streamlit frontend application
├── requirements.txt      # Python package dependencies
└── src
    ├── __init__.py
    ├── agent.py          # Core logic for all agents (Router, RAG, Summarize)
    ├── chain.py          # (Not used in final version, can be removed)
    └── main.py           # FastAPI server setup and API endpoint definitions
```

## ⚙️ Setup Instructions

Follow these steps to get the application running locally.

### 1. Prerequisites

-   Python 3.9+
-   Ollama installed and running.

### 2. Clone the Repository

```bash
git clone https://github.com/abhay-2108/AI-Microservices-with-LangChain-and-Ollama
cd AI Microservices with LangChain
```

### 3. Install LLM & Embedding Models

Pull the required models from Ollama. The application uses one model for generation (`llama3`) and another for embeddings (`nomic-embed-text`).

```bash
ollama pull mistral:7b
ollama pull nomic-embed-text:v1.5
```

You can verify the models are installed by running `ollama list`.

### 4. Set Up Python Environment

It's highly recommended to use a virtual environment to manage dependencies.

```bash
# Create a virtual environment
python -m venv venv

# Activate it (Linux/macOS)
source venv/bin/activate

# Activate it (Windows)
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the project root by copying the example file.


Your `.env` file should look like this. You can change `OLLAMA_MODEL` if you wish to use a different generative model.

```
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=mistral:7b
OLLAMA_EMBED_MODEL=nomic-embed-text:v1.5
```

## 🚀 How to Run

### Start the Backend Server

With your environment activated and Ollama running, start the FastAPI server using Uvicorn.

```bash
uvicorn src.main:app --reload
```

The server will start, and on the first run, it will create and cache the vector store from `data/document.txt`. This might take a moment. Subsequent startups will be much faster.

The API is now available at `http://127.0.0.1:8000`.

## 🧪 How to Test the API

You can interact with the API in several ways.

### 1. Interactive API Docs (Swagger UI)

Navigate to `http://127.0.0.1:8000/docs` in your browser to access the auto-generated Swagger UI. You can test all endpoints directly from this interface.

### 2. Postman

1.  Open Postman.
2.  Click `File > Import...` and select the `postman/AI_Services.postman_collection.json` file.
3.  The **AI Services** collection will appear, containing pre-configured requests for all three endpoints.

### 3. cURL

You can also test the endpoints from your terminal using `curl`.

#### Summarize Text

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/summarize' \
  -H 'Content-Type: application/json' \
  -d '{"text": "LangChain is a framework for developing applications powered by language models. It enables applications that are data-aware and agentic."}'
```

#### Question Answering (RAG)

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/qa' \
  -H 'Content-Type: application/json' \
  -d '{"question": "What is The Zen of Python?"}'
```

#### Generate Learning Path

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/learn-path' \
  -H 'Content-Type: application/json' \
  -d '{"profile": "I am a data analyst familiar with SQL and Tableau.", "goal": "I want to learn machine learning to build predictive models."}'
```