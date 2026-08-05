from sqlite3 import Connection



def create_chat_schema(connection: Connection) -> None:
    # Creating all the tables for the chat database

    cursor = connection.cursor()

    # Session table
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS sessions (
            session_id TEXT PRIMARY KEY,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        )
        '''
    )

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS messages (
            message_id TEXT PRIMARY KEY,
            session_id TEXT NOT NULL,
            created_at TEXT NOT NULL,
            role TEXT NOT NULL,
            message TEXT NOT NULL,

            FOREIGN KEY (session_id)
                REFERENCES sessions(session_id)
                ON DELETE CASCADE
        )
        '''
    )