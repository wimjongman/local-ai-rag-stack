from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import Chroma
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_community.document_loaders import TextLoader
import os

# Load and embed documents
loader = TextLoader("documents/example.txt")
docs = loader.load()

# Explicitly use a model that is pulled
embedding = OllamaEmbeddings(model="llama3")
db = Chroma.from_documents(docs, embedding)

# Setup LLM
llm = Ollama(model="llama3")
qa = RetrievalQA.from_chain_type(llm=llm, retriever=db.as_retriever())

# Query
while True:
    query = input("Q: ")
    if query.lower() in ("exit", "quit"): break
    answer = qa.run(query)
    print(f"A: {answer}\n")
