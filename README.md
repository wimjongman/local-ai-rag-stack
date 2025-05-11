# Local AI RAG Stack

Run a full local AI environment with:
- Ollama for model runtime (e.g., LLaMA 3)
- OpenWebUI as a chat interface for Ollama (accessible at http://localhost:3000)
- LangChain + Chroma as a basic RAG pipeline for question answering over local documents

## Quickstart

### Clone the repository with submodules
```bash
git clone https://github.com/wimjongman/local-ai-rag-stack.git
cd local-ai-rag-stack
```

If you forgot `--recurse-submodules`:
```bash
git submodule update --init --recursive
```

Add the open webui submodule manually:
```bash
git submodule add https://github.com/open-webui/open-webui.git openwebui
git submodule update --init --recursive
```

### Start Ollama + Web UI
```bash
docker-compose up -d
```

### Activate RAG script
```bash
cd rag
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

Ask questions about your own documents locally 🚀
