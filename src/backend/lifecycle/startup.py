from backend.database.initialize import initialize_database
from backend.database.schema import (
    create_chat_schema,
    create_planner_schema,
    create_pipeline_schema,
    create_paper_schema,
    create_system_schema
)



def startup() -> None:
    # Peroform backend startup tasks

    initialize_database(
        [
            create_chat_schema,
            create_planner_schema,
            create_pipeline_schema,
            create_paper_schema,
            create_system_schema
        ]
    )