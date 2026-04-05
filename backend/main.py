from fastapi import FastAPI
from pydantic import BaseModel
from agents.orchestrator import run_agent

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    response = run_agent(req.message)
    return {"response": response}
