from fastapi import FastAPI,Query
from app.rag.engine import RAGEngine


app=FastAPI()

rag_engine=RAGEngine()

@app.get("/query")
def query(question=Query(...,description="user question")):
    # return response based on the pdf content
    try:
        answer=rag_engine.generate_answer(question)
        return {
            "question":question,
            "answer":answer
        }
    except Exception as e:
        return {
            "question":question,
            "answer":None,
            "error":str(e)
        }
