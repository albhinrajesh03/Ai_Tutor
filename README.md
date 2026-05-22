AI Tutor:

A RAG-based AI Tutor built using:
- Python
- FastAPI
- ChromaDB
- Sentence Transformers
- CrossEncoder Reranking
- Groq API
- PDF processing

Features:
- PDF text extraction
- Text chunking
- Semantic search
- Reranking for better retrieval accuracy
- AI-powered responses using Groq LLM
- REST API with FastAPI
- Interactive API testing through Swagger UI (`/docs`)
- Strict document-based answering (reduces hallucinations)

Project Workflow:

User Question
↓
Retrieve relevant chunks from document
↓
Rerank retrieved chunks
↓
Build prompt with context
↓
Send prompt to Groq LLM
↓
Return final answer

Requirements:
Before running this project, make sure these are installed:
- Python
- Required packages
Install dependencies:
```bash
pip install -r requirements.txt
```

Environment Setup:
Create a `.env` file in the project root:
```.env
GROQ_API_KEY=your_api_key_here
```

Run Project:

Start FastAPI server:
```bash
python -m uvicorn api:app --reload
```

After running, open:
API documentation:
```text
http://localhost:8000/docs
```

Tech Stack:
- FastAPI → API backend
- ChromaDB → Vector database
- Sentence Transformers → Embedding generation
- CrossEncoder → Reranking
- Groq → LLM inference
- PyPDF → PDF text extraction