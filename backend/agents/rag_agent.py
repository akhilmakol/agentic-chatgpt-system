from tools.vector_store import search_vectors

def retrieve_context(query: str):
    docs = search_vectors(query)
    return "\n".join(docs)
