from uuid import uuid4



class SessionManager:
    # Create new session
    def create_session(self) -> str:
        return str(uuid4)

    # Checking if the session already exists or not
    def session_exists(self, session_id: str) -> bool:
        # PLACEHOLDER
        return True

    # Retrieves the requested session
    def get_session(self, session_id: str) -> dict:
        # PLACEHOLDER
        return { 'session_id': session_id }