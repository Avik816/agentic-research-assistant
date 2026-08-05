# PLACEHOLDER CODE FOR NOW

from backend.data_schemas.request import ChatRequest
from backend.data_schemas.response import ChatResponse



class ChatService:
    # Processes a user's request and returns a formatted response
    def process_request(self, request: ChatRequest) -> ChatResponse:
        return ChatResponse(
            success = True,
            session_id = request.session_id,
            response = 'Chat Service Initialized Successfully.'
        )
