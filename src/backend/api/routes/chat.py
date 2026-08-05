from fastapi import APIRouter
from backend.data_schemas.request import ChatRequest
from backend.data_schemas.response import ChatResponse
from backend.services.chat_service import ChatService



router = APIRouter()

@router.post(
    '/chat',
    response_model=ChatResponse
)

# Handles the incomming chat requests
async def chat(request: ChatRequest) -> ChatResponse:
    chat_service = ChatService()

    return chat_service.process_request(request=request)