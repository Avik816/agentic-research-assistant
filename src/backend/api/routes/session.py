from fastapi import APIRouter
from backend.session.session_manager import create_reai_session



session_router = APIRouter(prefix = '/session', tags = ['session'])

@session_router.post('/')
def create_session():
    # Creates a new ReAI session
    
    session_id = create_reai_session()

    return (
        {
            'success': True,
            'session_id': session_id
        }
    )