AI Tutor:
A RAG-based AI Tutor built using Python, FastAPI, ChromaDB, Sentence Transformers, CrossEncoder reranking, and a local LLM.

Features:
- PDF text extraction
- Text chunking
- Semantic search using embeddings
- CrossEncoder reranking for better retrieval quality
- AI-powered responses using a local LLM
- FastAPI REST API
- Interactive API testing through Swagger UI (`/docs`)
- Conversation history support
- Debug endpoint for retrieval inspection


Project Workflow:
User Question
↓
Retrieve relevant chunks from document
↓
Rerank retrieved chunks
↓
Build prompt using:
    - Retrieved context
    - Previous conversation history
↓
Send prompt to LLM
↓
Return final answer


Tech Stack:
- Python → Core programming language
- FastAPI → API backend
- ChromaDB → Vector database
- Sentence Transformers → Embedding generation
- CrossEncoder → Retrieval reranking
- Local LLM → Response generation
- PyPDF → PDF text extraction


Requirements:
Before running this project, install:
- Python
- Required Python packages
Install dependencies:
```bash
pip install -r requirements.txt
```


Setup:
Place your PDF file inside the project directory:
```text
Book.pdf
```


Run Project:
Start FastAPI server:
```bash
python -m uvicorn api:app
```


API Documentation:
After running, open:
```text
http://localhost:8000/docs
```
Swagger UI allows interactive testing of endpoints.


Available Endpoints:
- Ask question
    POST
    ```text
    /question
    ```
    Request:
    ```json
    {
        "question":"What is operators?"
    }
    ```
    Response:
    ```json
    {
        "answer":"Operators are..."
    }
    ```

- Debug retrieval
    POST

    ```text
    /debug
    ```
    Request:

    ```json
    {
        "question":"Operators"
    }
    ```
    Response:
    ```json
    {
        "question":"Operators",
        "retrieved_result":[...],
        "history":[...]
    }
    ```


Current Architecture:
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
LLM
↓
Response
