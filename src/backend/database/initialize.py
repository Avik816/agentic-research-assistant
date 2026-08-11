from typing import Callable
from sqlite3 import Connection
from backend.database.connection import get_connection
from utils.enums import Database



def initialize_database(
        database: Database,
        schema_function: Callable[[Connection], None]
    ) -> None:
    # Initializing the requested database

    connection = get_connection(database)

    try:
        schema_function(connection)
        connection.commit()

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()