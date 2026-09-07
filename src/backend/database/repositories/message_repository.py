from datetime import datetime
from uuid import uuid4
from backend.database.connection import get_connection



def create_message(
        session_id: str,
        role: str,
        message:str
) -> str:
    # Creates and stores messages for particular sessions

    message_id = str(uuid4)
    created_at = datetime.now()
    connection = get_connection()

    try:
        cursor = connection.cursor()
        cursor.execute(
            '''
                INSERT INTO messages (
                    message_id,
                    session_id,
                    role,
                    created_at,
                    message
                )
                VALUES (%s, %s, %s, %s, %s)
            ''',
            (
                message_id,
                session_id,
                role,
                created_at,
                message
            )
        )

        connection.commit()
        cursor.close()

        return message_id

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()


def get_message(message_id: str):
    # Retrieves a single messages using its Message ID

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            '''
                SELECT *
                FROM messages
                WHERE message_id = %s
            ''',
            (message_id,)
        )

        message = cursor.fetchone()
        cursor.close()

        return message

    finally:
        connection.close()


def get_messages(session_id: str):
    # Retrieves all messages using its Message ID

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            '''
                SELECT *
                FROM messages
                WHERE session_id = %s
                ORDER BY created_at ASC
            ''',
            (session_id,)
        )

        messages = cursor.fetchall()
        cursor.close()

        return messages

    finally:
        connection.close()


# If message needs to be deleted code to be added here