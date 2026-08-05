from backend.database.connection import get_connection
from backend.database.schema import create_chat_schema



def initialize_chat_database() -> None:
    # Initializing the chat database
    # Creating the entire chatbase-related transactions

    connection = get_connection()

    try:
        create_chat_schema(connection=connection)
        connection.commit()

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()