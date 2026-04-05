import faiss
import numpy as np

documents = [
    "Agentic AI automates workflows using multiple agents",
    "RAG improves LLM accuracy using external knowledge",
    "JIRA stories define agile software requirements"
]

dimension = 384
index = faiss.IndexFlatL2(dimension)

vectors = np.random.rand(len(documents), dimension).astype("float32")
index.add(vectors)

def search_vectors(query: str):
    query_vector = np.random.rand(1, dimension).astype("float32")
    _, indices = index.search(query_vector, k=2)
    return [documents[i] for i in indices[0]]
