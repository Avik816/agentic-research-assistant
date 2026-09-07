# from src.engine.utils.paths import PLANNER_ROLE
from ollama import chat
import json



PLANNER_ROLE = 'src/engine/planner/role.txt'
with open(PLANNER_ROLE, 'r', encoding='utf-8') as f:
    planner_role = f.read()


def run_planner(user_query: str):
    response = chat(
        model = 'qwen2.5:3b',
        messages = [
            {
                'role': 'system',
                'content': planner_role,
            },
            {
                'role': 'user',
                'content': user_query,
            },
        ],
        options = {
            'temperature': 0.0,
        },
    )

    return response['message']['content']






query = input('Enter your query: ')

result = json.loads(run_planner(query))

pipeline = result['execution_plan'][0]['pipeline']

print('\nPlanner Response:\n')
print(type(result))
print(result)
print(pipeline)