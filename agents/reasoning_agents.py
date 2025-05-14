from utils.logger import logger

class PlannerAgent:
    @staticmethod
    def run(state):
        logger.info("Planning Completed: Delegating to DataIngestionAgent")
        state['next_agent'] = "DataIngestionAgent"
        return state