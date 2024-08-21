import json
from typing import List
from app.ai.agents import TravelAgent
from app.ai.schemas import AgentMessage, AgentStreamingEvent
from app.ai.enums import AgentStreamingEventTypeEnum
from app.ai.prompts import TravelAgentPrompts
from app.utils.logging import AppLogger
from .base import BaseService

logger = AppLogger().get_logger()

class TravelAgentService(BaseService):
    def __init__(self):
        self.agent = TravelAgent()
        pass
    
    async def chat(self, messages: List[AgentMessage]):
        # tool_outputs = []
        async for chunk in self.agent.astreaming(messages=messages):            
            if chunk.type == AgentStreamingEventTypeEnum.MESSAGE:
                yield chunk.content