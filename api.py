from fastapi import FastAPI
from pydantic import BaseModel
from llm import ask_llm
from pdf_loader import load_pdf
from chromadb_reranker_rag import split_text, prepare_chunks, retrieve

text=load_pdf("Book.pdf")
chunks=split_text(text)
prepare_chunks(chunks)

app=FastAPI()

class Question(BaseModel):
    question:str

@app.post("/question")
def ask(data: Question):
    
    result=retrieve(data.question)
    context="\n".join(result)

    prompt= f"""
    You are a strict AI tutor.

    Your job:
        - Teach only using the given context
        - If context is insufficient, say: "Not found in the document"
        - Never hallucinate or assume information

    Response style:
        - Simple explanation
        - Step-by-step format
        - Use examples if possible

    Context: {context}
    User Question:{data.question}
    """
    answer=ask_llm(prompt)

    return {"answer":answer}