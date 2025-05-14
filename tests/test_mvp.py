import unittest
from orchestration.agent_graph import AgentOrchestrator
from memory.faiss_memory import Memory

class TestAgenticMVP(unittest.TestCase):

    def setUp(self):
        # Initialize orchestrator and memory for testing
        self.orchestrator = AgentOrchestrator()
        self.memory = Memory()

    def test_agent_execution_flow(self):
        """Test if agents execute successfully and final state contains expected keys."""
        final_state = self.orchestrator.run_flow()
        self.assertIn('data', final_state, "Data not found in final state!")
        self.assertTrue(final_state.get('data').strip() != "", "Data is empty after processing!")

    def test_memory_storage_and_search(self):
        """Test FAISS memory store and search functionality."""
        sample_text = "Artificial Intelligence is transforming industries."
        self.memory.store_embedding("test_key", sample_text)

        distances, indices = self.memory.search("transforming AI", top_k=1)
        self.assertIsNotNone(distances, "Memory search returned None!")
        self.assertGreaterEqual(distances[0][0], 0, "Invalid distance found in search result!")

    def test_empty_memory_search(self):
        """Test search behavior when memory is empty."""
        empty_memory = Memory()
        distances, indices = empty_memory.search("No embeddings here", top_k=1)
        self.assertIsNone(distances, "Expected None for empty memory search.")

if __name__ == "__main__":
    unittest.main()