import sqlite3, os
from dotenv import load_dotenv



# Loading .env variables
load_dotenv()

def get_connection() -> sqlite3.Connection:
    # Setting up the database connection for Chat Subsystem
    db_type = os.getenv('CHAT_DB_TYPE')
    db_path = os.getenv('CHAT_DB_PATH')

    # Check for database and its path
    if db_type != 'CHAT_DB_TYPE':
        raise ValueError(f'Unsupported Database Type: {db_type}.')
    if not db_path:
        raise ValueError('Path for chat database is NOT configured.')

    connection = sqlite3.connect(db_path)

    return connection