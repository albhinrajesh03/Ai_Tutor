from fastapi import FastAPI
from pydantic import BaseModel
from llm import ask_llm
from pdf_loader import load_pdf
from chromadb_reranker_rag import split_text, prepare_chunks, retrieve
from memory import set_memory, get_memory

text=load_pdf("Book.pdf")
chunks=split_text(text)
prepare_chunks(chunks)

app=FastAPI()

class Question(BaseModel):
    question:str

@app.post("/question")
def ask(data: Question):
    
    result=retrieve(data.question)

    if not result:
        return {
        "question": data.question,
        "retrieved_result": [],
        "answer": "Not found in document"
    }


    context="\n".join(result)
    history= get_memory()

    prompt= f"""
    You are a strict AI tutor.

    Your job:
        - Be a tutor.
        - Use Previous Conversation while answering, if possible.
        - Do not use your own knowledge. If the answer is not in the context, Reply exactly: "Not found in document".

    Response style:
        - Simple explanation.
        - Step-by-step format.
        - Use examples if possible.

    Previous Conversation: {history}
    Context: {context}
    User Question: {data.question}
    """
    answer=ask_llm(prompt)

    set_memory()

    return {
            "answer": answer,
            "source": result,
        }



@app.post("/debug")
def debug(data: Question):

    result=retrieve(data.question)

    return {
        "question": data.question,
        "retrieved_result": result,
    }