from typing import List
from pydantic import BaseModel
from app.ai.schemas import AgentMessage

class ChatRequestSchema(BaseModel):
    messages: List[AgentMessage]
    
