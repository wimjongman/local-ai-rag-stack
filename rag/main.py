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
