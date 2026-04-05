from fastapi import FastAPI
from pydantic import BaseModel
from agents.orchestrator import run_agent

app = FastAPI(title="Agentic ChatGPT API")

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "Agentic ChatGPT API running 🚀"}

@app.post("/chat")
def chat(req: ChatRequest):
    response = run_agent(req.message)
    return {"response": response}
