import os
import psycopg2
from dotenv import load_dotenv



load_dotenv()

def get_connection():
    # Creates and returns a connection to the ReAI PostgreSQL database

    db_type = os.getenv("DB_TYPE")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")

    if not db_type:
        raise ValueError('Database Type is not configured.')
    if db_type.lower() != 'PostgreSQL':
        raise ValueError(f'Unsupported databse type: {db_type}')

    required_config = {
        'DB_HOST': db_host,
        'DB_PORT': db_port,
        'DB_NAME': db_name,
        'DB_USER': db_user,
        'DB_PASSWORD': db_password,
    }

    for config_name, config_value in required_config.items():
        if not config_value:
            raise ValueError(f'{config_name} is not configured.')


    return psycopg2.connect(
        host = db_host,
        port = db_port,
        database = db_name,
        user = db_user,
        password = db_password
    )