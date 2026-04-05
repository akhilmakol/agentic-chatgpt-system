import faiss
import numpy as np

docs = [
    "Agentic AI helps automate workflows",
    "RAG improves LLM accuracy",
    "JIRA stories define software requirements"
]

index = faiss.IndexFlatL2(384)
vectors = np.random.rand(len(docs), 384).astype("float32")
index.add(vectors)

def search_vectors(query):
    q = np.random.rand(1, 384).astype("float32")
    _, I = index.search(q, 2)
    return [docs[i] for i in I[0]]
