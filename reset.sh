#!/bin/bash

set -e

echo "Stopping and removing containers..."
docker compose down -v || true

echo "Removing cloned project directory (if applicable)..."
cd ..
rm -rf local-ai-rag-stack || true

echo "Removing Ollama Docker volume..."
# List all volumes: docker volume ls
# You can replace 'ollama_data' below with the actual volume name if needed

docker volume rm ollama_data || true

echo "Done. You can now clone the repository fresh."
