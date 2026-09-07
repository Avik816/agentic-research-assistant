from typing import Callable
from backend.database.connection import get_connection



def initialize_database(schema_functions: list[Callable]) -> None:
    # Initializing the ReAI database

    connection = get_connection()

    try:
        for schema_function in schema_functions:
            schema_function(connection)

        connection.commit()

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()