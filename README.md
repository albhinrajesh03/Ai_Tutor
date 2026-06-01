# AI Tutor

A RAG-based AI Tutor built using Python, FastAPI, ChromaDB, Sentence Transformers, CrossEncoder reranking, and a local LLM.

## Features

* PDF text extraction
* Text chunking
* Semantic search using embeddings
* CrossEncoder reranking for improved retrieval accuracy
* AI-powered responses using a local LLM
* FastAPI REST API
* Interactive API testing through Swagger UI (`/docs`)
* Persistent conversation memory using `history.txt`
* Context-aware responses using previous conversations

---

## Project Workflow

User Question

↓

Retrieve relevant chunks from document

↓

Rerank retrieved chunks

↓

Load previous conversation history

↓

Build prompt using:

* Retrieved context
* Conversation memory

↓

Send prompt to LLM

↓

Generate answer

↓

Save conversation to memory

↓

Return response

---

## Tech Stack

* Python → Core programming language
* FastAPI → API backend
* ChromaDB → Vector database
* Sentence Transformers → Embedding generation
* CrossEncoder → Retrieval reranking
* Local LLM → Response generation
* PyPDF → PDF text extraction
* File-based Memory (`history.txt`) → Conversation persistence

---

## Requirements

Before running this project, install:

* Python
* Required Python packages

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Setup

Place your PDF file inside the project directory:

```text
Book.pdf
```

---

## Run Project

Start the FastAPI server:

```bash
python -m uvicorn api:app --reload
```

---

## API Documentation

After starting the server, open:

```text
http://localhost:8000/docs
```

Swagger UI allows interactive testing of all endpoints.

---

## Available Endpoints

### Ask Question

**POST**

```text
/question
```

Request:

```json
{
  "question": "What is an operator?"
}
```

Response:

```json
{
  "answer": "Operators are symbols used to perform operations on variables and values."
}
```

---

## Memory System

Conversation history is stored in:

```text
history.txt
```

Each completed conversation is saved and can be loaded later to provide context-aware responses.

Example:

```text
User: What is a string?
Ai: A string is a sequence of characters.
---END---

User: What is an operator?
Ai: Operators are symbols used to perform operations.
---END---
```

The AI can use recent conversations while answering new questions.

---

## Current Architecture

User

↓

FastAPI

↓

RAG Pipeline

↓

ChromaDB Retrieval

↓

CrossEncoder Reranking

↓

Conversation Memory

↓

Prompt Construction

↓

Local LLM

↓

Response

↓

Save to Memory

↓

Return Answer

---

## Future Improvements

* Multi-user chat sessions
* User authentication
* Streaming responses
* Chat history database integration
* Web-based frontend
* Source citations in answers
* Agentic workflows and tool calling