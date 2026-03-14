import os
from pathlib import Path

from dotenv import load_dotenv

CONFIG_DIR = os.path.expanduser("~/.config/taiga-cli")
TOKEN_PATH = os.path.join(CONFIG_DIR, "token")


def load_env():
    """Carrega variáveis de ambiente do .env local, se existir."""
    env_path = Path(__file__).parent.parent / ".env"
    if env_path.exists():
        load_dotenv(dotenv_path=env_path, override=True)


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
    print(f"[DEBUG] TAIGA_PROJECT_ID (raw): {os.environ.get('TAIGA_PROJECT_ID')}")
    return os.environ.get("TAIGA_PROJECT_ID")
