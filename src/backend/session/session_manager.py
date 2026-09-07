from backend.database.repositories.session_repository import (
    create_session,
    get_session,
    update_session
)



def create_reai_session() -> str:
    # Creating new ReAI Session.
    session_id = create_session()


    return session_id


def get_reai_session(session_id: str):
    # Retrieves the existing ReAI Session
    session = get_session(session_id)


    return session


def update_reai_session(session_id: str) -> None:
    # Updates the activity timestamp of a ReAI session
    update_session(session_id)