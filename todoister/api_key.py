import os
from pathlib import Path

from dotenv import dotenv_values


class ApiKeyNotFound(Exception):
    """Raise when Api Key was not found with the usual ways"""


def load_api_key(api_key_file: Path):
    if api_key_file.exists():
        return api_key_file.read_text().strip()
    return get_api_key_from_env_file()


def get_api_key_from_env_file():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    envs = dotenv_values(os.path.join(dir_path, ".env"))

    api_key = envs.get("TODOIST_API_KEY")
    if api_key is None:
        raise ApiKeyNotFound("Could not load Todoist API Key")
    return api_key
