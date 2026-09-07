from backend.data_schemas.request import ChatRequest
from backend.data_schemas.response import ChatResponse
from backend.session.session_manager import (
    get_reai_session,
    update_reai_session
)
from backend.database.repositories.message_repository import create_message



def process_request(request: ChatRequest) -> ChatResponse:
    
    session = get_reai_session(request.session_id)

    # Checks wether ReAI session exists
    if session is None:
        return ChatResponse (
            success = False,
            session_id = request.session_id,
            response = 'ReAI does not exists'
        )

    # Storing user's message
    create_message(
        session_id = request.session_id,
        role = 'user',
        message = request.message
    )

    # Update session activity
    update_reai_session(request.session_id)


    # PLACEHOLDER for Engine
    return ChatResponse(
        success = True,
        session_id = request.session_id,
        response = 'Chat Service Initialized Successfully'
    )