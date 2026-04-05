import faiss
import numpy as np
from tools.embeddings import get_embedding

documents = []
index = faiss.IndexFlatL2(384)

def add_documents(docs):
    global documents
    documents.extend(docs)

    vectors = np.array([get_embedding(d) for d in docs]).astype("float32")
    index.add(vectors)

def search_vectors(query, k=2):
    query_vector = np.array([get_embedding(query)]).astype("float32")
    _, indices = index.search(query_vector, k)
    return [documents[i] for i in indices[0]]
