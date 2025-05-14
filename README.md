🤖 Agentic AI MVP

A Modular, Multi-Agent AI System that simulates autonomous collaboration between specialized agents to perform data processing, memory management, and reasoning tasks. This project serves as a foundational architecture for building intelligent enterprise automation systems, decision support platforms, and future agent-based AI solutions.

---

📚 **Project Overview**

This MVP demonstrates how different types of agents—each with a specialized role—work together to:

- Ingest, clean, validate, and store data.
- Generate embeddings and store them in a local vector memory using FAISS.
- Retrieve and reason over stored information.
- Simulate decision-making processes.
- Easily extend to include interactive APIs and advanced reasoning models.

---
 🏗️ **Architecture Overview**

| Layer              | Technology/Tool Used                |
|--------------------|-------------------------------------|
| Agent Framework    | LangGraph, Custom Python Classes    |
| Agent Categories   | Data Agents, Knowledge Agents, Reasoning Agents, Action Agents |
| Memory & Storage   | FAISS (Vector Similarity Search), SQLite/TinyDB (optional) |
| Embeddings         | Hugging Face Sentence Transformers (`all-MiniLM-L6-v2`) |
| Language Models    | GPT4All / Llama.cpp (Provisioned for Local LLM Integration) |
| API Layer (Optional)| FastAPI (For interactive queries)  |
| Logging            | Custom Python Logger (`utils/logger.py`) |
| Testing            | Python `unittest` Framework         |
| Containerization   | Docker (For easy deployment)        |
| Version Control    | Git & GitHub                        |

---
 🚀 **How It Works**

1. **Planner Agent** initiates the workflow and delegates tasks.
2. **Data Agents** process raw data through ingestion, cleaning, validation, and formatting stages.
3. **Knowledge Agents** store processed data as embeddings and enable semantic search through FAISS.
4. **Reasoning Agents** simulate basic decision-making and manage task flows.
5. **Action Agents** (planned for future) will generate reports and send notifications.
6. Final results are stored, and logs capture the workflow execution.

---
 📦 **Installation & Setup**

```bash
# Clone the Repository
git clone https://github.com/Cholaking/agenticai_mvp.git
cd agentic_ai_mvp

# Install Dependencies
pip install -r requirements.txt

# Run the Application
python main.py
![image](https://github.com/user-attachments/assets/6d7c4e0b-98c9-464d-bd3b-fbf32b992305)
