from fastapi import FastAPI
from app.schemas import ChatRequest, ChatResponse
from app.agent import vulnerable_agent, secure_agent

app = FastAPI(title="LLM Sentinel", version="0.1.0",
              description="Local-only AI agent security testing lab")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    agent = secure_agent if request.mode == "secure" else vulnerable_agent
    result = agent(request.tenant_id, request.user_id, request.message)
    return ChatResponse(**result)
