from fastapi import APIRouter, Depends, Request
from fastapi.responses import StreamingResponse
from app.utils.logging import AppLogger
from app.services.travel_agent import TravelAgentService
from app.exceptions.http_exception import NotFoundHTTPException
from .schema import ChatRequestSchema

logger = AppLogger().get_logger()

router = APIRouter(
    prefix="/travel", tags=["Travel Agent"], responses={404: {"error": "Not found"}}
)


@router.post("/chat")
async def get_user(model: ChatRequestSchema):
    """
    Chat interface for travel agent.
    """
    travel_service = TravelAgentService()
    return StreamingResponse(
        travel_service.chat(messages=model.messages),
        media_type="text/plain"
    )
    # return tenant_model