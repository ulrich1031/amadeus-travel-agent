from openai import AsyncAzureOpenAI
from app.config import Settings, get_settings

class AzureOpenAIClient:
    
    def __init__(self, settings: Settings = get_settings()):
        self.settings = settings
        self.client = AsyncAzureOpenAI(
            azure_endpoint = self.settings.AZURE_OPENAI_ENDPOINT, 
            api_key=self.settings.AZURE_OPENAI_API_KEY,  
            api_version=self.settings.OPENAI_API_VERSION
        )

    async def ainvoke(self, **kwargs):
        if 'model' not in kwargs:
            kwargs['model'] = self.settings.SMART_LLM_MODEL
            
        response = await self.client.chat.completions.create(
            **kwargs
        )
        
        return response.choices[0].message.content

    async def astream(self, **kwargs):
        if 'model' not in kwargs:
            kwargs['model'] = self.settings.SMART_LLM_MODEL
            
        stream = await self.client.chat.completions.create(
            **kwargs,
            stream=True
        )
        
        async for chunk in stream:
            if chunk.choices and len(chunk.choices) > 0:
                content = chunk.choices[0].delta.content
                if content:
                    yield content