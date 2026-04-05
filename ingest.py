import os

def load_documents(folder="backend/data/docs"):
    docs = []
    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        if file.endswith(".txt"):
            with open(path, "r", encoding="utf-8") as f:
                docs.append(f.read())
    return docs

if __name__ == "__main__":
    docs = load_documents()
    print("Loaded docs:", len(docs))
