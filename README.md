# Local AI RAG Stack

Run a full local AI environment with:
- Ollama for model runtime (e.g., LLaMA 3)
- OpenWebUI as a chat interface for Ollama (accessible at http://localhost:3000)
- LangChain + Chroma as a basic RAG pipeline for question answering over local documents

## Quickstart

### Clone the repository
```bash
git clone https://github.com/wimjongman/local-ai-rag-stack.git
cd local-ai-rag-stack
```

### Pull the LLM model
If you have not installed Ollama on your host system (for CLI usage), install it first:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Then pull the model:
```bash
ollama pull llama3
```

### Start Ollama + Web UI
To start the containers:
```bash
docker-compose up -d
```

#### 🪟 Access from Windows if using WSL
If you're running this inside WSL and can't reach http://localhost:3000 from Windows:
1. Run this in WSL to find your IP:
   ```bash
   ip addr show eth0 | grep inet
   ```
2. Use the resulting IP (e.g. `http://172.20.5.234:3000`) in your Windows browser.

This allows you to access the OpenWebUI interface from Windows via the WSL network.

docker compose build openwebui

### Activate RAG script
```bash
cd rag
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python main.py
```

Ask questions about your own documents locally 🚀
