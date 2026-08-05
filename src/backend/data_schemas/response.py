from pydantic import BaseModel



class ChatResponse(BaseModel):
    success: bool       # Tells the backend whether the request completed successfully
    session_id: str
    response: str


# Schema building left:
# downloaded papers, execution progress, or references