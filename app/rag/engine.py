from app.core.config import PDF_PATH , CHUNK_OVERLAP,CHUNK_SIZE,TOK_K,EMBEDDING_MODEL_NAME
from app.rag.loader import PDFLoader
from app.rag.chunker import LangchainTextChunker
from app.rag.vector_store import VectorStore
from app.rag.embeddings import EmbeddingModel

from langchain.agents import create_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv



class RAGEngine:

    def __init__(self):
        self.vector_store=None
        self.llm=None
        self.initialize()
    def initialize(self):
        load_dotenv()
        text=PDFLoader(PDF_PATH).load()
        chunks=LangchainTextChunker(CHUNK_SIZE,CHUNK_OVERLAP).chunk(text)
        embeddings=EmbeddingModel(EMBEDDING_MODEL_NAME)
        self.vector_store=VectorStore(embeddings)
        self.vector_store.build(chunks)

        self.llm=ChatGroq(model_name="llama-3.3-70b-versatile")
    

    def generate_answer(self,question:str):
        contexts =self.vector_store.search(query=question,k=TOK_K)
        combine_text="\n\n".join(contexts)

        prompt_template=f"""
you are a helpfull assistant. use only the information provider in the context below to answer. if the answer is not present in the context, respond with " I don't know" .

Context :{combine_text}

question :  {question}

answer :
"""
        # agent=create_agent(
        #     model=self.llm,
        #     system_prompt="you are a helpfull assistant"
        # )
        # result =agent.invoke({
        #     "messages":[
        #         {"role":"user","content":prompt_template}
        #     ]
        # })
        # return result["messages"][-1].content

        response=self.llm.invoke(prompt_template)
        return response.content

        






