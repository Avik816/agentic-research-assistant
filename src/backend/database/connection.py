import sqlite3, os
from dotenv import load_dotenv
from utils.enums import Database



# Loading .env variables
load_dotenv()

def get_connection(database: Database) -> sqlite3.Connection:
    # Setting up the database connection for Chat Subsystem
    db_type = os.getenv(f'{database.value}_DATABASE_TYPE')
    db_path = os.getenv(f'{database.value}_DATABASE_PATH')

    # Check for database and its path is valid or not
    if not db_type:
        raise ValueError(f'{database.value}_DATABASE_TYPE is not configured.')

    if not db_path:
        raise ValueError(f'{database.value}_DATABASE_PATH is not configured.')

    # Checking the database type
    if db_type.lower() != 'sqlite':
        raise ValueError(f'Unsupported database type: {db_type}')
    

    return sqlite3.connect(db_path)