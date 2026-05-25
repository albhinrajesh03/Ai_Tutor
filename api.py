from fastapi import FastAPI
from pydantic import BaseModel
from llm import ask_llm
from pdf_loader import load_pdf
from chromadb_reranker_rag import split_text, prepare_chunks, retrieve

text=load_pdf("Book.pdf")
chunks=split_text(text)
prepare_chunks(chunks)

app=FastAPI()

chat_history=[]

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
    history="\n".join(chat_history)

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

    chat_history.append(f"User: {data.question}")
    chat_history.append(f"Ai: {answer}")


    return {
            "answer": answer,
            "source": result,
            "history": chat_history
        }



@app.post("/debug")
def debug(data: Question):

    result=retrieve(data.question)

    return {
        "question": data.question,
        "retrieved_result": result,
        "history": chat_history
    }