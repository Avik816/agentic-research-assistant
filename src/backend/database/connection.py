import os
from dotenv import load_dotenv
import psycopg2
from psycopg2 import OperationalError, sql



load_dotenv()


def create_ReAI_database(required_config):
    default_db = os.getenv('DEFAULT_DB')

    default_connection = psycopg2.connect(
        host = required_config['DB_HOST'],
        port = required_config['DB_PORT'],
        database = default_db,
        user = required_config['DB_USER'],
        password = required_config['DB_PASSWORD']
    )

    # Mandatory
    default_connection.autocommit = True

    cursor = default_connection.cursor()
    cursor.execute(
        sql.SQL('CREATE DATABASE {}').format(
            sql.Identifier(required_config['DB_NAME'])
        )
    )

    default_connection.close()

    
    return psycopg2.connect(
        host = required_config['DB_HOST'],
        port = required_config['DB_PORT'],
        database = required_config['DB_NAME'],
        user = required_config['DB_USER'],
        password = required_config['DB_PASSWORD']
    )


def get_server_connection(required_config):
    # Connects to the ReAI server using the default 'postgres' database.
    # This connection is used only for checking/creating the ReAI database.
    try:
        connection = psycopg2.connect(
            host = required_config['DB_HOST'],
            port = required_config['DB_PORT'],
            database = required_config['DB_NAME'],
            user = required_config['DB_USER'],
            password = required_config['DB_PASSWORD']
        )

        return connection

    except OperationalError as DbNotExists:
        pgcode = getattr(DbNotExists, 'pgcode', None)
        
        if pgcode == '3D000' or 'does not exists' in str(DbNotExists):
            print('Database does not exists.\nConfiguring Database.')

            # Creating ReAI database
            return create_ReAI_database(required_config)

        raise


def get_connection():
    # Creates and returns a connection to the ReAI PostgreSQL database

    db_type = os.getenv("DB_TYPE")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")

    if not db_type:
        raise ValueError('Database Type is not found in .env file.')
    if db_type.lower() != 'postgresql':
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
            raise ValueError(f'{config_name} is not found in .env file.')

    # Checks whether the database exists or not
       # If it does not exists creates it
    connection = get_server_connection(required_config)


    return connection