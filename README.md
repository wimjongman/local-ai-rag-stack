# Local AI RAG Stack

Run a full local AI environment with:
- Ollama for model runtime (e.g., LLaMA 3)
- OpenWebUI as a chat interface
- LangChain + Chroma as a basic RAG pipeline

## Quickstart
```bash
git clone https://github.com/wimjongman/local-ai-rag-stack.git
cd local-ai-rag-stack

# Start Ollama + Web UI
docker-compose up -d

# Activate RAG script
cd rag
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
