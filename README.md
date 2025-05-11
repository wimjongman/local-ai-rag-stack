## local-ai-rag-stack
A minimal setup to run a local LLM with Ollama, OpenWebUI, and a Python-based RAG pipeline (LangChain + Chroma).

### Structure:

```
local-ai-rag-stack/
├── .env
├── docker-compose.yml
├── openwebui/           # Submodule or local clone of OpenWebUI
├── ollama/              # Optional custom config
├── rag/
│   ├── main.py
│   ├── requirements.txt
│   └── documents/
│       └── example.txt
└── README.md
```

---

### docker-compose.yml
```yaml
version: '3.8'

services:
  ollama:
    image: ollama/ollama
    ports:
      - "11434:11434"
    volumes:
      - ollama_data:/root/.ollama
    deploy:
      resources:
        reservations:
          devices:
            - capabilities: ["gpu"]

  openwebui:
    image: ghcr.io/open-webui/open-webui:main
    ports:
      - "3000:3000"
    environment:
      - OLLAMA_BASE_URL=http://ollama:11434
    depends_on:
      - ollama

volumes:
  ollama_data:
```

---

### rag/requirements.txt
```txt
langchain
llama-index
chromadb
ollama
```

---

### rag/main.py
```python
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma
from langchain.embeddings import OllamaEmbeddings
from langchain.document_loaders import TextLoader
import os

# Load and embed documents
loader = TextLoader("documents/example.txt")
docs = loader.load()

embedding = OllamaEmbeddings()
db = Chroma.from_documents(docs, embedding)

# Setup LLM
llm = Ollama(model="llama3")
qa = RetrievalQA.from_chain_type(llm=llm, retriever=db.as_retriever())

# Query
while True:
    query = input("Vraag: ")
    if query.lower() in ("exit", "quit"): break
    answer = qa.run(query)
    print(f"Antwoord: {answer}\n")
```

---

### rag/documents/example.txt
```
Rembrandt was a Dutch painter and etcher. He is generally considered one of the greatest painters and printmakers in European art history.
```

---

### README.md (summary)
```markdown
# Local AI RAG Stack

Run a full local AI environment with:
- Ollama for model runtime (e.g., LLaMA 3)
- OpenWebUI as a chat interface
- LangChain + Chroma as a basic RAG pipeline

## Quickstart
```bash
git clone https://github.com/YOURNAME/local-ai-rag-stack.git
cd local-ai-rag-stack

# Start Ollama + Web UI
docker-compose up -d

# Activate RAG script
debian$ cd rag
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

Ask questions about your own documents locally 🚀
