# 🚀 Agentic ChatGPT System (FastAPI Backend)

A production-ready **Agentic AI backend system** built with FastAPI, enabling:

* 🤖 Multi-agent orchestration (SQL, API, JIRA, RAG)
* 🧠 Pluggable LLM (OpenAI / AWS Bedrock / Local models)
* 📄 Retrieval-Augmented Generation (RAG)
* ⚡ Scalable REST API for AI-powered applications

---

## 🧠 Architecture

```bash
Client (Postman / Curl / UI)
        ↓
FastAPI Backend (Agent Orchestrator)
        ↓
-----------------------------------
| Agents                          |
| - SQL Agent                     |
| - API Agent                     |
| - JIRA Generator                |
| - RAG Retriever                 |
-----------------------------------
        ↓
LLM (MiniGPT / OpenAI / Bedrock)
        ↓
Vector Store (FAISS / Pinecone)
```

---

## 📁 Project Structure

```bash
agentic-chatgpt-system/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   │
│   ├── agents/
│   │   ├── orchestrator.py
│   │   ├── sql_agent.py
│   │   ├── api_agent.py
│   │   ├── jira_agent.py
│   │   └── rag_agent.py
│   │
│   ├── tools/
│   │   ├── db.py
│   │   ├── vector_store.py
│   │   └── embeddings.py
│   │
│   ├── models/
│   │   └── llm.py
│   │
│   ├── schemas/
│   │   └── chat.py
│   │
│   └── data/
│       ├── sample.db
│       └── docs/
│
├── ingest.py
├── postman/
│   └── agentic-chatgpt.postman_collection.json
└── README.md
```

---

## ⚙️ Prerequisites

* Python 3.9+
* pip
* Virtual environment (recommended)

---

## 🚀 Setup & Run

### 🔹 1. Clone Repository

```bash
git clone https://github.com/akhilmakol/agentic-chatgpt-system.git
cd agentic-chatgpt-system/backend
```

---

### 🔹 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

> If PowerShell blocks activation:

```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
venv\Scripts\activate
```

---

### 🔹 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

---

### 🔹 4. Run FastAPI Server

```bash
python -m uvicorn main:app --reload
```

---

## 🌐 API Access

* Base URL:
  http://127.0.0.1:8000

* Swagger UI:
  http://127.0.0.1:8000/docs

---

## 🧪 API Usage

### 🔹 POST `/chat`

#### Request:

```json
{
  "message": "Create JIRA story for login feature"
}
```

#### Response:

```json
{
  "response": "Generated output..."
}
```

---

## 📦 Postman Collection

This repo includes a ready-to-use Postman collection:

```bash
postman/agentic-chatgpt.postman_collection.json
```

### 👉 How to Use

1. Open Postman
2. Click **Import**
3. Select the collection file

---

## 🧪 Sample Test Prompts

* "Create JIRA story for payment API"
* "Fetch SQL data from sales table"
* "Call API for latest crypto price"
* "Explain RAG architecture"

---

## 🧩 Agent Capabilities

### 🔹 SQL Agent

* Executes database queries
* Extendable to LLM-based Text-to-SQL

---

### 🔹 API Agent

* Calls external APIs
* Easily configurable for any REST service

---

### 🔹 JIRA Agent

Generates structured user stories:

* Title
* Description
* Acceptance Criteria
* Story Points

---

### 🔹 RAG Agent

* Retrieves context from documents
* Uses vector similarity search

---

## 📄 RAG (Document Support)

Add documents to:

```bash
backend/data/docs/
```

---

### 📥 Extend Ingestion

Use `ingest.py` to:

* Load PDFs
* Chunk content
* Generate embeddings
* Store in vector DB

---

## 🔧 LLM Integration

Update:

```bash
backend/models/llm.py
```

Supported options:

* OpenAI
* AWS Bedrock
* Hugging Face
* Local MiniGPT

---

## 🐳 Docker (Optional)

```bash
docker-compose up --build
```

---

## 🚀 Future Enhancements

* 🔄 Streaming responses (real-time)
* 🧠 Memory (chat history)
* 🔐 Authentication (JWT / OAuth)
* 📊 Observability & logging
* ☁️ AWS deployment (ECS / Lambda / Bedrock)
* 🧩 LangGraph multi-agent workflows

---

## 🧠 Tech Stack

* Backend: FastAPI
* Agents: Custom orchestration
* Vector Store: FAISS
* LLM: Pluggable

---

## 🤝 Contributing

Pull requests are welcome!

---

## 📜 License

MIT License

---

## 👨‍💻 Author

Built by Akhil Makol
AI | Data | Agentic Systems

---

## ⭐ Support

If you find this useful:

* ⭐ Star the repo
* 🔁 Share with your network
* 💡 Contribute ideas
