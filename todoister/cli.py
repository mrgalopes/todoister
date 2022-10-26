import sys

from todoist_api_python.api import TodoistAPI

from todoister.desktop_notify import notify
from todoister.api_key import get_api_key


def add_task():
    todo = sys.argv[1]
    if todo == "":
        exit(0)

    api_key = get_api_key()
    api = TodoistAPI(api_key)
    try:
        api.add_task(content=todo)
        notify(f"Adicionado: {todo}")
    except Exception as error:
        notify(f"Error: {error}")
        print(error)
