# taiga-cli

Modular CLI for Taiga project management (Hermes Conrad)

- Modern Python (3.10+)
- Typer for CLI
- httpx for API
- python-dotenv for env management
- OOP, modular, extensible


## Instalação

### Usando pipx (recomendado)

```bash
pipx install .
# ou, para instalar direto do repositório:
# pipx install git+https://github.com/maicondmenezes/taiga-cli.git
```

### Usando pip

```bash
python -m pip install .
# ou, para modo desenvolvimento:
python -m pip install -e .
```

### Usando uv

```bash
uv venv
uv pip install -e .
```

## Configuração Inicial

Após instalar, execute:

```bash
taiga configure
# Ou, se instalado em modo dev:
uv run taiga configure
```
Preencha a URL da API e o slug/ID do projeto conforme solicitado. As configurações ficam em ~/.config/taiga-cli/config.env.

## Uso

```bash
taiga --help
taiga list-projects
taiga login
# ... outros comandos disponíveis
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
