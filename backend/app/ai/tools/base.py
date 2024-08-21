from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool, tool
from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)

class BaseAgentTool(BaseTool):
    pass