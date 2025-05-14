from utils.logger import logger

class DataIngestionAgent:
    @staticmethod
    def run(state):
        logger.info("Data Ingestion Completed")
        state['data'] = " Sample Ingested Data "  # Added extra spaces for cleaning step demo
        return state

class DataCleaningAgent:
    @staticmethod
    def run(state):
        logger.info("Data Cleaning Completed")
        state['data'] = state['data'].strip()
        return state

class DataValidationAgent:
    @staticmethod
    def run(state):
        logger.info("Data Validation Completed")
        # Simple validation: check if data is not empty
        if not state.get('data'):
            raise ValueError("Data is empty after cleaning!")
        return state

class DataFormattingAgent:
    @staticmethod
    def run(state):
        logger.info("Data Formatting Completed")
        # Example: Convert text to uppercase
        state['data'] = state['data'].upper()
        return state

class DataStorageAgent:
    @staticmethod
    def run(state):
        logger.info("Data Storage Completed")
        # Simulating storage (in-memory)
        state['stored'] = True
        return state