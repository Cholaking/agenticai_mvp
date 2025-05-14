from utils.logger import logger
from memory.faiss_memory import Memory

class MemoryAgent:
    def __init__(self):
        self.memory = Memory()

    def run(self, state):
        logger.info("Storing Data in Memory")
        self.memory.store_embedding("sample_id", state['data'])
        return state

class RetrieverAgent:
    @staticmethod
    def run(state):
        logger.info("Retrieving Context from Memory")
        # Mock Retrieval
        state['context'] = "Retrieved Context"
        return state