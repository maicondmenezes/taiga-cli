import os
from pathlib import Path

from dotenv import load_dotenv

CONFIG_DIR = os.path.expanduser("~/.config/taiga-cli")
TOKEN_PATH = os.path.join(CONFIG_DIR, "token")
CONFIG_ENV_PATH = os.path.join(CONFIG_DIR, "config.env")
REFRESH_TOKEN_PATH = os.path.join(CONFIG_DIR, "refresh_token")


def save_refresh_token(refresh_token: str):
    os.makedirs(CONFIG_DIR, exist_ok=True)
    with open(REFRESH_TOKEN_PATH, "w") as f:
        f.write(refresh_token.strip())


def load_refresh_token() -> str | None:
    if os.path.exists(REFRESH_TOKEN_PATH):
        with open(REFRESH_TOKEN_PATH) as f:
            return f.read().strip()
    return None


def load_env():
    """Carrega variáveis de ambiente do .env local, se existir."""
    env_path = Path(__file__).parent.parent / ".env"
    if env_path.exists():
        load_dotenv(dotenv_path=env_path, override=True)

    # Carrega variáveis do arquivo de configuração persistente
    if os.path.exists(CONFIG_ENV_PATH):
        load_dotenv(dotenv_path=CONFIG_ENV_PATH, override=True)


def save_config_vars(api_url: str, project_id: str):
    os.makedirs(CONFIG_DIR, exist_ok=True)
    with open(CONFIG_ENV_PATH, "w") as f:
        f.write(f"TAIGA_API_URL={api_url}\n")
        f.write(f"TAIGA_PROJECT_ID={project_id}\n")


def save_token(token: str):
    os.makedirs(CONFIG_DIR, exist_ok=True)
    with open(TOKEN_PATH, "w") as f:
        f.write(token.strip())


def load_token() -> str | None:
    if os.path.exists(TOKEN_PATH):
        with open(TOKEN_PATH) as f:
            return f.read().strip()
    return None


def get_taiga_api_url() -> str:
    load_env()
    return os.environ.get("TAIGA_API_URL", "http://taiga-kanban/api/v1")


def get_taiga_project_id() -> str | None:
    load_env()
    return os.environ.get("TAIGA_PROJECT_ID")
