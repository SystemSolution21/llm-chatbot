# app/rag.py

# Import local modules
from app.config import EMBEDDING_MODEL, VECTOR_DB_PATH
from langchain_chroma import Chroma

# Import third-party modules
from langchain_huggingface import HuggingFaceEmbeddings

# Load the embedding model
embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

# Load the vector database
vectordb = Chroma(persist_directory=VECTOR_DB_PATH, embedding_function=embeddings)


# Retrieve context from the vector database
def retrieve_context(query: str) -> str:
    docs = vectordb.similarity_search(query, k=3)
    return "\n".join([d.page_content for d in docs])
