from pydantic import BaseModel, Field
from typing import Literal

class ChatRequest(BaseModel):
    tenant_id: str
    user_id: str
    message: str = Field(min_length=1, max_length=4000)
    mode: Literal["vulnerable", "secure"] = "vulnerable"

class ChatResponse(BaseModel):
    reply: str
    tool_executed: bool = False
    evidence: dict = {}
