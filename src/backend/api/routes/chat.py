from fastapi import APIRouter
from backend.data_schemas.request import ChatRequest
from backend.data_schemas.response import ChatResponse
from backend.services.chat_service import process_request



router = APIRouter(prefix = '/chat', tags = ['chat'])

@router.post(
    '/',
    response_model = ChatResponse
)

# Handles the incomming chat requests
async def chat(request: ChatRequest) -> ChatResponse:
    return process_request(request=request)