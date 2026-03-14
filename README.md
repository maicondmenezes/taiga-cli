# taiga-cli

Modular CLI for Taiga project management (Hermes Conrad)

- Modern Python (3.10+)
- Typer for CLI
- httpx for API
- python-dotenv for env management
- OOP, modular, extensible

## Usage

```bash
uv venv
uv pip install -e .
uv taiga --help
```

## Structure

- `taiga_cli/` — main package
  - `api.py` — API client abstractions
  - `models.py` — domain models (Task, Story, Epic, Initiative)
  - `services.py` — business logic/services
  - `cli.py` — Typer CLI entrypoints
  - `main.py` — CLI app loader

## Features
- Create/update/list tasks, stories, epics, initiatives
- Status management
- Extensible for new Taiga features
