# LangChain Ollama Chatbot

A simple AI chatbot built using LangChain, Ollama, and Streamlit. The application runs locally using Ollama models, allowing users to interact with an AI assistant without requiring OpenAI API credits.

## Features

* Local LLM integration using Ollama
* Streamlit-based interactive UI
* LangChain Prompt Templates
* Output Parsing using StrOutputParser
* Lightweight and beginner-friendly
* No cloud API dependency

## Tech Stack

* Python
* LangChain
* Ollama
* Streamlit

## Installation

### Clone Repository

```bash
git clone https://github.com/VanshSharma1/langchain-ollama-chatbot.git
cd langchain-ollama-chatbot
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install Ollama

Download from:

https://ollama.com/download

### Pull Model

```bash
ollama pull gemma3:1b
```

### Run Application

```bash
streamlit run app.py
```

## Project Workflow

User Input → Prompt Template → Ollama Model → Output Parser → Streamlit Interface

## Future Enhancements

* Chat History
* Memory Integration
* PDF Question Answering
* Retrieval-Augmented Generation (RAG)
* Multi-Model Support

## Author

Vansh Sharma

* B.Tech CSE
* Full Stack Developer
* AI & Generative AI Enthusiast
