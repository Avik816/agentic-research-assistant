from psycopg2.extensions import connection



def create_chat_schema(connection: connection) -> None:
    # Create tables required for chat functionality

    cursor = connection.cursor()

    cursor.execute(
        '''
            CREATE TABLE IF NOT EXISTS sessions ('
                session_id TEXT PRIMARY KEY,
                created_at TIMESTAMP NOT NULL,
                updated_at TIMESTAMP NOT NULL
            )
        '''
    )

    cursor.execute(
        '''
            CREATE TABLE IF NOT EXISTS messages (
                message_id TEXT PRIMARY KEY,
                session_id TEXT NOT NULL,
                role TEXT NOT NULL,
                created_at TIMESTAMP NOT NULL,
                message TEXT NOT NULL,

                FOREIGN KEY (session_id) 
                    REFERENCES sessions (session_id)
                    ON DELETE CASCADE
            )
        '''
    )

    cursor.close()


# Will be added later.
def create_planner_schema(connection: connection) -> None:
    pass


def create_pipeline_schema(connection: connection) -> None:
    pass


def create_paper_schema(connection: connection) -> None:
    pass


def create_system_schema(connection: connection) -> None:
    pass