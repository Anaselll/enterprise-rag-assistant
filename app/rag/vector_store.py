from langchain_community.vectorstores import FAISS


class VectorStore:
    "Faiss based vector store for document retrieval"

    def __init__(self,embeddings):
        self.embeddings=embeddings
        self.store=None
    def build(self,texts):
        self.store=FAISS.from_texts(
            texts=texts,
            embedding=self.embeddings.model
        )
    def search(self,query,k =3):
        if self.store is None:
            raise ValueError("Vector store still not initialized")
        docs=self.store.similarity_search(query,k=k)
        return [doc.page_content for doc in docs ]