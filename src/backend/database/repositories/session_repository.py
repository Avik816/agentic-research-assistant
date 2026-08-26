from datetime import datetime
from uuid import uuid4
from backend.database.connection import get_connection



def create_session() -> str:
    # Creates a new session in the databse and returns it

    session_id = str(uuid4())
    current_time = datetime.now()
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            '''
                INSERT INTO sessions (
                    session_id,
                    created_at,
                    updated_at
                )
                VALUES (%s, %s, %s)
            ''',
            (
                session_id,
                current_time,
                current_time
            )
        )

        connection.commit()
        cursor.close()

        return session_id

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()


def get_session(session_id: str):
    # Retrieves the Session Id.

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            '''
                SELECT session_id, created_at, updated_at
                FROM sessions
                WHERE session_id = %s
            ''',
            (session_id,)
        )

        session = cursor.fetchone()
        cursor.close()

        return session

    finally:
        connection.close()


def update_session(session_id: str) -> None:
    # Updates the session's update_at timestamp

    current_time = datetime.now()
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            '''
                UPDATE sessions
                SET update_at = %s
                WHERE session_id = %s
            ''',
            (current_time, session_id)
        )

        connection.commit()
        cursor.close()

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()


def delete_session(session_id: str) -> None:
    # Deletes a session by ID.

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            '''
                DELETE FROM sessions
                WHERE session_id = %s
            ''',
            (session_id,)
        )

        connection.commit()
        cursor.close()

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()