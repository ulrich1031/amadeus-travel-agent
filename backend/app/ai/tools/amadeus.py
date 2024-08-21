import httpx
from typing import Type, Optional
from app.utils.amadus import AmadeusTravelAPIWrapper
from .base import Field, BaseModel, BaseAgentTool
from app.utils.logging import AppLogger

logger = AppLogger().get_logger()

class AmadeusAPIRequestInput(BaseModel):
    endpoint: str = Field(description='Amadeus API endpoint to send request to.')
    method: str = Field(description='Amadeus API request method')
    body: Optional[dict] = Field(description='Request body for the endpoint.', default={})
    headers: Optional[dict] = Field(description="Request header for the endpoint excluding authorization header.", default={})
    number_of_results: Optional[int] = 5
    
class AmadeusAPITool(BaseAgentTool):
    name = 'amadeus_api_tool'
    description = 'useful when you have to interact with Amadeus API for travel APIs.'
    args_schema: Type[BaseModel] = AmadeusAPIRequestInput
    api_wrapper: AmadeusTravelAPIWrapper
    
    def _run(
        self,
        endpoint: str,
        method: str,
        query_params: Optional[dict] = {},
        body: Optional[dict] = {},
        headers: Optional[dict] = {},
        number_of_results: Optional[int] = 5
    ):
        raise NotImplemented
    
    async def _arun(
        self,
        endpoint: str,
        method: str,
        query_params: Optional[dict] = {},
        body: Optional[dict] = {},
        headers: Optional[dict] = {},
        number_of_results: Optional[int] = 5
    ):
        if 'Authorization' in headers:
            del headers['Authorization']
        
        try:  
            results = await self.api_wrapper.request(  
                endpoint=endpoint,  
                method=method,  
                query_params=query_params,  
                body=body,  
                additional_headers=headers  
            )
            if isinstance(results, list):
                results = results[:number_of_results]
            if isinstance(results, dict):  
                for key in results:  
                    if isinstance(results[key], list):  
                        results[key] = results[key][:number_of_results]  
                        
            return results
        except httpx.HTTPStatusError as e:  
            return {  
                "error": f"HTTP error occurred: {e.response.status_code}",  
                "details": e.response.json()  # or e.response.text for raw response  
            }  
        except httpx.RequestError as e:  
            return {  
                "error": "An error occurred while making the request",  
                "details": str(e)  
            }  
        except Exception as e:
            return {  
                "error": "An unexpected error occurred",  
                "details": str(e)  
            } 