import httpx
from app.utils.logging import AppLogger
from app.config import get_settings

logger = AppLogger().get_logger()

class AmadeusTravelAPIWrapper:  
    
    def __init__(self):  
        self.settings = get_settings()  
        self.token_url = 'https://test.api.amadeus.com/v1/security/oauth2/token'  
        self.access_token = None  
    
    async def _get_access_token(self):  
        data = {  
            'grant_type': 'client_credentials',  
            'client_id': self.settings.AMADEUS_API_KEY,  
            'client_secret': self.settings.AMADEUS_API_SECRET  
        }  
        headers = {  
            'Content-Type': 'application/x-www-form-urlencoded'  
        }   
        
        timeout = httpx.Timeout(10.0, read=20.0)  # Increase timeout settings  

        async with httpx.AsyncClient(timeout=timeout) as client:  
            try:  
                response = await client.post(self.token_url, data=data, headers=headers)  
                response.raise_for_status()  # Raises exception if status code isn't 200  
                token_info = response.json()  
                self.access_token = token_info['access_token'] 
                logger.info(self.access_token)
            except httpx.HTTPStatusError as exc:  
                logger.error(f"HTTP error occurred: {exc.response.status_code} - {exc.response.text}")  
                raise  
            except httpx.RequestError as exc: 
                logger.error(exec)  
                raise  
    
    async def request(self, endpoint: str, method='GET', query_params=None, body=None, additional_headers=None):  
        if self.access_token is None:  
            await self._get_access_token()  

        if endpoint.startswith("/") == False:
            endpoint = "/" + endpoint
        
        url = f"https://test.api.amadeus.com{endpoint}"  
        headers = {  
            'Authorization': f'Bearer {self.access_token}'  
        }  
        if additional_headers:  
            headers.update(additional_headers)  

        timeout = httpx.Timeout(10.0, read=20.0)  # Increase timeout settings  
        
        async with httpx.AsyncClient(timeout=timeout) as client:  
            try:  
                if method.upper() == 'GET':  
                    response = await client.get(url, params=query_params, headers=headers)  
                elif method.upper() == 'POST':  
                    response = await client.post(url, params=query_params, json=body, headers=headers)  
                elif method.upper() == 'PUT':  
                    response = await client.put(url, params=query_params, json=body, headers=headers)  
                elif method.upper() == 'PATCH':  
                    response = await client.patch(url, params=query_params, json=body, headers=headers)  
                elif method.upper() == 'DELETE':  
                    response = await client.delete(url, params=query_params, headers=headers)  
                else:  
                    raise ValueError(f"Unsupported HTTP method: {method}")  
                
                response.raise_for_status()  
                return response.json()  
            except httpx.HTTPStatusError as exc:  
                logger.error(f"HTTP error occurred: {exc.response.status_code} - {exc.response.text}")  
                raise  
            except httpx.RequestError as exc:  
                logger.error(exc)  
                raise exc