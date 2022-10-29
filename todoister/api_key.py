import os
from pathlib import Path

from dotenv import dotenv_values

from todoister.desktop_notify import notify

DEFAULT_FILE = Path.home() / ".todoist_api_key"

def get_api_key():
    api_key = get_api_key_from_file()
    if api_key is not None:
        return api_key
    return get_api_key_from_env_file()

def get_api_key_from_file():
    if not DEFAULT_FILE.exists():
        return None
    return DEFAULT_FILE.read_text().strip()

def get_api_key_from_env_file():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    envs = dotenv_values(os.path.join(dir_path, ".env"))

    api_key = envs.get("TODOIST_API_KEY")
    if api_key is None:
        notify("Error", "Could not load Todoist API Key")
        exit(1)
    return api_key
