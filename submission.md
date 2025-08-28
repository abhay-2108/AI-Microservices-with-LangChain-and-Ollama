# Internship Assignment Submission

**Submitted by:** Abhay Tiwari 

**Project Title:** AI Microservices with LangChain

---

## GitHub Repository Link

The complete source code for this project is available on GitHub at the following URL:

[https://github.com/abhay-2108/AI-Microservices-with-LangChain-and-Ollama](https://github.com/abhay-2108/AI-Microservices-with-LangChain-and-Ollama)

---

## Project Explanation

This project implements a multi-agent AI system designed as a collection of microservices. It leverages local Large Language Models (LLMs) via Ollama to ensure privacy and eliminate reliance on paid APIs.

The core of the system is a **Router Agent** that analyzes incoming user queries and delegates them to the most appropriate specialized agent. The system includes two such specialist agents:

1.  **RAG (Retrieval-Augmented Generation) Agent**: This agent answers questions by retrieving relevant information from a local document store (a ChromaDB vector database). It is designed to provide context-aware answers based on a specific knowledge base.

2.  **Summarization Agent**: This agent is responsible for condensing long pieces of text into concise summaries.

### Technical Architecture

-   **Backend**: Built with **FastAPI** and **LangServe**, exposing each agent as a distinct API endpoint. This microservice architecture allows for scalability and easy integration.
-   **AI/LLM**: Powered by **LangChain** for agent creation and orchestration. It uses local models (e.g., `mistral:7b`) run through **Ollama**.
-   **Frontend**: A simple and interactive user interface created with **Streamlit**, which communicates with the FastAPI backend to provide a seamless user experience.
-   **Vector Store**: **ChromaDB** is used for efficient storage and retrieval of text embeddings for the RAG agent.

The project demonstrates a practical, end-to-end implementation of an agentic AI system, from local model hosting to a functional web interface.