import os
from tools.vector_store import add_documents

def load_documents(folder="backend/data/docs"):
    docs = []
    for file in os.listdir(folder):
        if file.endswith(".txt"):
            with open(os.path.join(folder, file), "r", encoding="utf-8") as f:
                docs.append(f.read())
    return docs

if __name__ == "__main__":
    docs = load_documents()
    add_documents(docs)
    print("Documents indexed:", len(docs))
