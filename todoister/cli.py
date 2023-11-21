import click

from todoist_api_python.api import TodoistAPI

from todoister.desktop_notify import notify
from todoister.api_key import load_api_key


@click.command(help="Adds task to Todoist inbox")
@click.argument("todo")
def add_task(todo):
    api = TodoistAPI(load_api_key())
    try:
        api.add_task(content=todo)
        notify("Todo added", f"{todo}")
    except Exception as error:
        notify("Error", f"{error}")
        print(error)
