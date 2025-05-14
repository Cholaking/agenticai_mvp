import yaml
from agents.data_agents import DataIngestionAgent, DataCleaningAgent
from agents.knowledge_agents import MemoryAgent, RetrieverAgent
from agents.reasoning_agents import PlannerAgent
from utils.logger import logger

class AgentOrchestrator:
    def __init__(self, config_path='configs/agent_config.yaml'):
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)
        self.agent_map = {
            "DataIngestionAgent": DataIngestionAgent(),
            "DataCleaningAgent": DataCleaningAgent(),
            "MemoryAgent": MemoryAgent(),
            "RetrieverAgent": RetrieverAgent(),
            "PlannerAgent": PlannerAgent(),
        }

    def run_flow(self):
        state = {}
        current_agent = "PlannerAgent"

        for _ in range(5):  # Simulate 5 steps in the workflow
            agent = self.agent_map[current_agent]
            state = agent.run(state)
            current_agent = state.get('next_agent', "DataCleaningAgent")

        logger.info("Final State: %s", state)
        return state