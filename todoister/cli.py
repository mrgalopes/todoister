import sys
from pathlib import Path

import click
from todoist_api_python.api import TodoistAPI

from todoister.api_key import load_api_key
from todoister.desktop_notify import notify

DEFAULT_API_KEY_FILE = Path.home() / ".todoist_api_key"


@click.command(help="Adds task to Todoist inbox")
@click.argument("todo")
@click.option(
    "--notify",
    "should_notify",
    default=True,
    show_default=True,
    help="Send desktop notification on success or failure",
)
@click.option(
    "--api-key-file",
    "-k",
    "api_key_file",
    default=DEFAULT_API_KEY_FILE,
    show_default=True,
    type=click.Path(exists=True, path_type=Path),
    help="File containing Todoist API Key",
)
def add_task(todo, should_notify, api_key_file):
    try:
        api = TodoistAPI(load_api_key(api_key_file))
        api.add_task(content=todo)
        if should_notify:
            notify("Todo added", f"{todo}")
    except Exception as error:
        print(error, file=sys.stderr)
        if should_notify:
            notify("Error", f"{error}")
        exit(1)
