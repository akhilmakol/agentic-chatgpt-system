import os

structure = {
    "backend/agents": ["orchestrator.py", "sql_agent.py", "api_agent.py", "jira_agent.py", "rag_agent.py"],
    "backend/tools": ["db.py", "vector_store.py", "embeddings.py"],
    "backend/models": ["llm.py"],
    "backend/schemas": ["chat.py"],
    "backend/data/docs": [],
    "frontend/app": ["page.js"],
    "frontend/styles": ["globals.css"]
}

files = {
    "backend/main.py": "from fastapi import FastAPI\napp = FastAPI()\n\n@app.get('/')\ndef root(): return {'status':'running'}",
    "backend/requirements.txt": "fastapi\nuvicorn\npydantic\nrequests\nfaiss-cpu\nnumpy",
    "frontend/package.json": '{ "name": "agentic-ui", "version": "1.0.0" }',
    "README.md": "# Agentic ChatGPT System\n\nFull stack AI agent system.",
    ".gitignore": "venv/\nnode_modules/\n__pycache__/"
}

def create():
    for path, filenames in structure.items():
        os.makedirs(path, exist_ok=True)
        for f in filenames:
            open(os.path.join(path, f), "w").close()

    for path, content in files.items():
        with open(path, "w") as f:
            f.write(content)

if __name__ == "__main__":
    create()
    print("✅ Project structure created successfully!")