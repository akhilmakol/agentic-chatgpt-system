from fastapi import FastAPI
from schemas.chat import ChatRequest
from agents.orchestrator import run_agent

app = FastAPI(title="Agentic ChatGPT API")

@app.get("/")
async def home():
    return {"status": "running"}

@app.post("/chat")
async def chat(req: ChatRequest):
    response = run_agent(req.message)
    return {"response": response}
