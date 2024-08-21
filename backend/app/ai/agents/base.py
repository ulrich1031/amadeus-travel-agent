from datetime import datetime
from typing import List, AsyncGenerator
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langgraph.graph.graph import CompiledGraph
from app.utils.logging import AppLogger
from app.config import get_settings
from ..schemas import AgentStreamingEvent, AgentMessage
from ..enums import AgentStreamingEventTypeEnum, AgentMessageRoleTypeEnum

logger = AppLogger().get_logger()

class BaseAgent:

    def __init__(
        self,
        **kwargs
    ):
        self.settings = get_settings()
            
        self.model = ChatOpenAI(
            model=self.settings.SMART_LLM_MODEL,
            api_key=self.settings.OPENAI_API_KEY
        )

    def __get_agent_messages__(self, messages: List[AgentMessage]):
        return ([SystemMessage(content=self.system_prompt)] if self.system_prompt else []) + [
            HumanMessage(content=message.content) if message.role == AgentMessageRoleTypeEnum.USER.value  
            else AIMessage(content=message.content) if message.role == AgentMessageRoleTypeEnum.ASSISTANT.value  
            else None
            for message in messages
        ]
    
    async def __execute_agent_streaming__(self, agent_name: str, agent_executor: CompiledGraph, messages: List[AgentMessage]) -> AsyncGenerator[AgentStreamingEvent, None]:
        """  
        Execute agent streaming.  
        
        This method streams events associated with the execution of an agent. The events provide detailed information  
        about the agent's state, such as starting, ending, and intermediate processing.  

        Parameters:
         
            agent_name (str): The name of the agent being executed.  
            
            agent_executor (CompiledGraph): The executor handling the agent's compiled graph.  
            
            messages (List): A list of messages to be processed by the agent.  

        Yields:
            
            AgentStreamingEvent: Contains the type of the event, the name of the agent/tool, and relevant data such as content, inputs, and outputs.

        Event Types and Data:  


            1. `on_chain_start`:  
                - Indicates the start of the agent's chain.  
                - Data:   
                    - `type`: CHAIN_START  
                    - `name`: The name of the agent.  

            2. `on_chain_end`:  
                - Indicates the end of the agent's chain.  
                - Data:  
                    - `type`: CHAIN_END  
                    - `name`: The name of the agent.  
                    - `output`: The output message content from the agent.  

            3. `on_chat_model_stream`:  
                - Represents the streaming of messages from the chat model.  
                - Data:  
                    - `type`: MESSAGE  
                    - `content`: The content of the streamed message.  

            4. `on_tool_start`:  
                - Indicates the start of a tool associated with the agent.  
                - Data:  
                    - `type`: TOOL_START  
                    - `name`: The name of the tool.  
                    - `input`: The input data for the tool.  

            5. `on_tool_end`:  
                - Indicates the end of a tool's execution.  
                - Data:  
                    - `type`: TOOL_END  
                    - `name`: The name of the tool.  
                    - `output`: The output data from the tool.    
        """
        agent_span = None
        final_response = ""
        
        async for event in agent_executor.astream_events(
            {"messages": self.__get_agent_messages__(messages)}, version="v1"
        ):
            kind = event["event"]
            if kind == "on_chain_start":
                if (
                    event["name"] == agent_name
                ):
                    logger.info(f"Starting agent: {event['name']} with input: {event['data'].get('input')}")
                        
                    # logger.info(event)
                    yield AgentStreamingEvent(
                        type=AgentStreamingEventTypeEnum.CHAIN_START,
                        name=event['name']
                    )
                    
            elif kind == "on_chain_end":
                if (
                    event["name"] == agent_name
                ):
                    
                    logger.info(f"Done agent: {event['name']} with output: {event['data'].get('output')}")

                    yield AgentStreamingEvent(
                        type=AgentStreamingEventTypeEnum.CAHIN_END,
                        name=event['name'],
                        # output=final_response
                        output=event['data'].get('output').get('agent').get('messages')[0].content
                    )
                    
            if kind == "on_chat_model_stream":
                content = event["data"]["chunk"].content
                if content:
                    final_response = final_response + content
                    yield AgentStreamingEvent(
                        type=AgentStreamingEventTypeEnum.MESSAGE,
                        content=content
                    )
                    
            elif kind == "on_tool_start":
                logger.info(f"Starting tool: {event['name']} with inputs: {event['data'].get('input')}")
                    
                yield AgentStreamingEvent(
                    type=AgentStreamingEventTypeEnum.TOOL_START,
                    name=event['name'],
                    input=event['data'].get('input')
                )
                
            elif kind == "on_tool_end":
                logger.info(f"Done tool: {event['name']}")
                logger.info(f"Tool output was: {event['data'].get('output')}")
                    
                yield AgentStreamingEvent(
                    type=AgentStreamingEventTypeEnum.TOOL_END,
                    name=event['name'],
                    output=event['data'].get('output')
                )
                