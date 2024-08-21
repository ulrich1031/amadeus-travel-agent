from typing import Optional, Any, List, Dict
from pydantic import BaseModel
from ..enums import AgentStreamingEventTypeEnum

class AgentMessage(BaseModel):
    content: str
    role: str
    tool_data: Optional[Dict] = None

class AgentStreamingEvent(BaseModel):
    """
    Agent Streaming Event.
    
    Parameters:

        type (AgentStreamingEventTypeEnum): type of the event.
        
        name (Optional[str]): agent name or tool name.
        
        content (Optional[str]): llm response message chunk. type is "message"
        
        input (Optional[Any]): input of tool or agent
        
        output (Optional[Any]): output of tool or agent
    """
    type: AgentStreamingEventTypeEnum
    name: Optional[str] = None
    content: Optional[str] = None
    input: Optional[Any] = None
    output: Optional[Any] = None