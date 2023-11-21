import sys

import click
from todoist_api_python.api import TodoistAPI

from todoister.api_key import load_api_key
from todoister.desktop_notify import notify


@click.command(help="Adds task to Todoist inbox")
@click.argument("todo")
@click.option(
    "--notify",
    "should_notify",
    default=True,
    show_default=True,
    help="Send desktop notification on success or failure",
)
def add_task(todo, should_notify):
    try:
        api = TodoistAPI(load_api_key())
        api.add_task(content=todo)
        if should_notify:
            notify("Todo added", f"{todo}")
    except Exception as error:
        print(error, file=sys.stderr)
        if should_notify:
            notify("Error", f"{error}")
        exit(1)
