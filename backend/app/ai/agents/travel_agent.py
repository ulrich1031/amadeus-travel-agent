from typing import List, AsyncGenerator
from langgraph.prebuilt import create_react_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from app.utils.logging import AppLogger
from app.utils.amadus import AmadeusTravelAPIWrapper
from ..prompts import TravelAgentPrompts
from ..tools import AmadeusAPITool
from ..schemas import AgentStreamingEvent, AgentMessage
from ..enums import AgentStreamingEventTypeEnum, AgentMessageRoleTypeEnum
from .base import BaseAgent

logger = AppLogger().get_logger()

class TravelAgent(BaseAgent):
    
    def __init__(self):
        super().__init__()
        
        self.amadeus_api_wrapper = AmadeusTravelAPIWrapper()
        self.amadeus_tool = AmadeusAPITool(api_wrapper=self.amadeus_api_wrapper)
        
        self.tavil_tool = TavilySearchResults()
        
        self.tools = [
            self.amadeus_tool,
            self.tavil_tool
        ]
        
        self.agent_name = "travel-agent"
        self.agent_exectutor = self.agent_executor = create_react_agent(self.model, self.tools).with_config({"run_name": self.agent_name})
        self.system_prompt = TravelAgentPrompts.system_prompt()
    
    async def astreaming(self, messages: List[AgentMessage]) -> AsyncGenerator[AgentStreamingEvent, None]:
        
        async for chunk in self.__execute_agent_streaming__(
            agent_name=self.agent_name,
            agent_executor=self.agent_executor,
            messages=messages
        ):
            yield chunk
    
    