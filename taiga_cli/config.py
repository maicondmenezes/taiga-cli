
import os
from pathlib import Path

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



def _read_config_env() -> dict:
    """Lê o arquivo config.env e retorna um dicionário com as variáveis."""
    config = {}
    if os.path.exists(CONFIG_ENV_PATH):
        with open(CONFIG_ENV_PATH) as f:
            for line in f:
                if line.strip() and not line.strip().startswith("#"):
                    if "=" in line:
                        k, v = line.strip().split("=", 1)
                        config[k.strip()] = v.strip()
    return config


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
    config = _read_config_env()
    return config.get("TAIGA_API_URL", "http://taiga-kanban/api/v1")



def get_taiga_project_id() -> str | None:
    config = _read_config_env()
    return config.get("TAIGA_PROJECT_ID")
