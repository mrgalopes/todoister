# Todoister

Simple project to add a task to the Todoist inbox. Reads API key from either:

- ~/.todoist_api_key (only thing in the file);
- TODOIST_API_KEY environment variable

## Instalation

Using pipx:

```sh
pipx install git+https://github.com/mrgalopes/todoister.git
```

## Usage

If installed using pipx:

```sh
python -m todoister "Buy some eggs"
```

Else, do:

```sh
python -m todoister "Buy some eggs"
```

Using poetry:

```sh
poetry run python -m todoister "Buy some eggs"
```

## To-dos

- [ ] Add tests
- [ ] Run linter and formatter pre-commit
- [ ] Make cli more flexible
  - Add more commands, perhaps?
- [ ] Add option to skip desktop notification
