import faiss
from sentence_transformers import SentenceTransformer

from utils.logger import logger


# noinspection PyArgumentList
class Memory:
    def __init__(self, dim=384):  # Use 384 for 'all-MiniLM-L6-v2' model embeddings
        self.index = faiss.IndexFlatL2(dim)
        self.data = {}
        self.embedder = SentenceTransformer('all-MiniLM-L6-v2')  # Load embedding model

    def store_embedding(self, key, data_text):
        vec = self.embedder.encode([data_text]).astype('float32')
        if vec.shape[1] != self.index.d:
            raise ValueError(f"Embedding dimension mismatch. Expected: {self.index.d}, Got: {vec.shape[1]}")
        self.index.add(vec)
        self.data[key] = vec
        logger.info(f"Stored embedding for key: {key}")
        return vec

    def search(self, query_text, top_k=1):
        if self.index.ntotal == 0:
            logger.warning("Memory is empty. No embeddings to search.")
            return None, None

        query_vector = self.embedder.encode([query_text]).astype('float32')
        distances, indices = self.index.search(query_vector, top_k)
        logger.info(f"Search completed. Top-k: {top_k}")
        return distances, indices