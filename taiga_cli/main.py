import re

import httpx
import typer

from .api import TaigaAPI
from .config import (
    get_taiga_api_url,
    get_taiga_project_id,
    load_refresh_token,
    load_token,
    save_config_vars,
    save_refresh_token,
    save_token,
)
from .enums import (
    get_epic_status_id_by_name,
    get_task_status_id_by_name,
    get_user_story_status_id_by_name,
)
from .services import TaigaService

app = typer.Typer()


# --- CLI Commands ---


@app.command()
def configure():
    """
    Configura o Taiga CLI solicitando TAIGA_API_URL e
    TAIGA_PROJECT_ID e salvando em arquivo de configuração.
    """
    api_url = typer.prompt("Informe a URL da API do Taiga (ex: http://localhost:8000/api/v1/)")
    project_id = typer.prompt("Informe o slug ou ID do projeto Taiga")
    save_config_vars(api_url, project_id)
    typer.echo("[OK] Configuração salva em ~/.config/taiga-cli/config.env")


@app.command()
def list_projects():
    """Lista todos os projetos acessíveis ao usuário autenticado."""
    api_url = get_taiga_api_url()
    token = load_token()
    if not api_url:
        typer.echo("TAIGA_API_URL não definido no .env")
        raise typer.Exit(1)
    try:
        url = f"{api_url.rstrip('/')}/projects"
        headers = {"Authorization": f"Bearer {token}"} if token else {}
        resp = httpx.get(url, headers=headers, timeout=30.0)
        resp.raise_for_status()
        data = resp.json()
        if not data:
            typer.echo("Nenhum projeto encontrado.")
            return
        for proj in data:
            typer.echo(f"ID: {proj['id']} | Nome: {proj['name']} | Slug: {proj['slug']}")
    except Exception as e:
        typer.echo(f"[ERRO] Falha ao listar projetos: {e}")
        raise typer.Exit(1)


@app.command()
def login():
    """Solicita usuário e senha, autentica no Taiga e salva o token de acesso e refresh_token."""
    api_url = get_taiga_api_url()
    if not api_url:
        typer.echo("TAIGA_API_URL não definido. Execute 'taiga configure' primeiro.")
        raise typer.Exit(1)

    username = typer.prompt("Usuário do Taiga")
    password = typer.prompt("Senha do Taiga", hide_input=True)

    try:
        resp = httpx.post(
            f"{api_url.rstrip('/')}/auth",
            json={"type": "normal", "username": username, "password": password},
            timeout=30.0,
        )
        resp.raise_for_status()
        data = resp.json()
        token = data.get("auth_token")
        refresh_token = data.get("refresh") or data.get("refresh_token")
        save_token(token)
        typer.echo("[OK] Token salvo em ~/.config/taiga-cli/token")
        if refresh_token:
            save_refresh_token(refresh_token)
            typer.echo("[OK] Refresh token salvo em ~/.config/taiga-cli/refresh_token")
    except Exception as e:
        typer.echo(f"[ERRO] Falha ao autenticar: {e}")
        raise typer.Exit(1)


def ensure_token():
    """Garante que o token está válido, usando refresh_token se necessário."""
    token = load_token()
    if token:
        return token
    refresh_token = load_refresh_token()
    if not refresh_token:
        typer.echo("Token expirado ou ausente. Faça login novamente.")
        raise typer.Exit(1)
    api_url = get_taiga_api_url()
    try:
        resp = httpx.post(
            f"{api_url.rstrip('/')}/auth/refresh",
            json={"refresh": refresh_token},
            timeout=30.0,
        )
        resp.raise_for_status()
        data = resp.json()
        token = data.get("auth_token") or data.get("access")
        new_refresh = data.get("refresh") or data.get("refresh_token")
        if token:
            save_token(token)
        if new_refresh:
            save_refresh_token(new_refresh)
        typer.echo("[OK] Token renovado com sucesso.")
        return token
    except Exception as e:
        typer.echo(f"[ERRO] Falha ao renovar token: {e}")
        raise typer.Exit(1)


@app.command()
def get_project_id():
    """Busca o ID numérico do projeto Taiga pelo slug informado em TAIGA_PROJECT_ID."""
    project_id = get_taiga_project_id()
    api_url = get_taiga_api_url()
    token = load_token()
    if not project_id:
        typer.echo("TAIGA_PROJECT_ID não definido no .env")
        raise typer.Exit(1)
    try:
        url = f"{api_url.rstrip('/')}/projects/by_slug?slug={project_id}"
        headers = {"Authorization": f"Bearer {token}"} if token else {}
        resp = httpx.get(url, headers=headers, timeout=30.0)
        resp.raise_for_status()
        data = resp.json()
        typer.echo(f"ID numérico do projeto '{project_id}': {data['id']}")
    except Exception as e:
        typer.echo(f"[ERRO] Falha ao buscar ID do projeto: {e}")
        raise typer.Exit(1)


@app.command()
def hello():
    """Test CLI."""
    typer.echo("Taiga CLI is working!")


@app.command()
def list_epics():
    """List all epics in the project."""
    token = load_token()
    api_url = get_taiga_api_url()
    project_id = get_taiga_project_id()
    # ...
    api = TaigaAPI(api_url, token)
    service = TaigaService(api)
    if not project_id:
        typer.echo("TAIGA_PROJECT_ID not set in .env")
        raise typer.Exit(1)
    epics = service.list_epics(int(project_id))
    for e in epics:
        typer.echo(f"[{e.id}] {e.subject} | Status: {e.status}")


@app.command()
def list_initiatives():
    """List all initiatives (swimlanes) in the project."""
    api_url = get_taiga_api_url()
    token = load_token()
    project_id = get_taiga_project_id()
    api = TaigaAPI(api_url, token)
    service = TaigaService(api)
    if not project_id:
        typer.echo("TAIGA_PROJECT_ID not set in .env")
        raise typer.Exit(1)
    initiatives = service.list_initiatives(int(project_id))
    for i in initiatives:
        typer.echo(f"[{i.id}] {i.name} | Order: {i.order}")


@app.command()
def update_task(task_id: str, status: str = typer.Option(None), subject: str = typer.Option(None)):
    """Update a task by ID."""
    token = ensure_token()
    api_url = get_taiga_api_url()
    # ...
    api = TaigaAPI(api_url, token)
    data = {}
    if status:
        try:
            data["status"] = get_task_status_id_by_name(status)
        except ValueError as e:
            typer.echo(f"[ERRO] {e}")
            raise typer.Exit(1)
    if subject:
        data["subject"] = subject
    try:
        api.patch(f"tasks/{task_id}", data)
        typer.echo(f"[OK] Task {task_id} updated.")
    except httpx.HTTPStatusError as e:
        typer.echo(f"[ERRO] Falha ao atualizar task: {e.response.text}")
        raise typer.Exit(1)


@app.command()
def update_story(
    story_id: str, status: str = typer.Option(None), subject: str = typer.Option(None)
):
    """Update a story by ID."""
    token = ensure_token()
    api_url = get_taiga_api_url()
    project_id = get_taiga_project_id()
    # ...
    if not project_id:
        typer.echo("TAIGA_PROJECT_ID não definido.")
        raise typer.Exit(1)

    import re

    # Permitir busca por tag TS-XXX
    if re.fullmatch(r"TS-\d+", story_id, re.IGNORECASE):
        api = TaigaAPI(api_url, token)
        service = TaigaService(api)
        try:
            story = service.get_story_by_tag_full(story_id, int(project_id))
        except ValueError as e:
            typer.echo(f"[ERRO] {e}")
            raise typer.Exit(1)
        real_id = story["id"]
        version = story["version"]
    else:
        real_id = story_id
        version = None

    api = TaigaAPI(api_url, token)
    data = {}
    if version is not None:
        data["version"] = version
    if status:
        try:
            data["status"] = get_user_story_status_id_by_name(status)
        except ValueError as e:
            typer.echo(f"[ERRO] {e}")
            raise typer.Exit(1)
    if subject:
        data["subject"] = subject

    try:
        resp = api.client.patch(
            f"{api_url.rstrip('/')}/userstories/{real_id}", headers=api._headers(), json=data
        )
        resp.raise_for_status()
        typer.echo(f"[OK] Story {real_id} updated.")
    except httpx.HTTPStatusError as e:
        typer.echo(f"[ERRO] Falha ao atualizar story: {e.response.text}")
        raise typer.Exit(1)


@app.command()
def update_epic(
    epic_tag: str,
    status: str = typer.Option(None, help="Novo status (nome, ex: 'In progress')"),
    status_id: int = typer.Option(None, help="Novo status (id numérico)"),
    subject: str = typer.Option(None, help="Novo título do épico"),
    description: str = typer.Option(None, help="Nova descrição do épico"),
    assigned_to: int = typer.Option(None, help="ID do usuário responsável"),
    tags: str = typer.Option(None, help="Tags separadas por vírgula"),
):
    """
    Atualiza um épico pela tag (ex: EP-02).
    Permite atualizar status, título, descrição, responsável e tags.
    """
    project_id = get_taiga_project_id()
    if not project_id:
        typer.echo("TAIGA_PROJECT_ID not set in .env")
        raise typer.Exit(1)

    if not re.fullmatch(r"EP-\d+", epic_tag, re.IGNORECASE):
        typer.echo("[ERRO] O código do épico deve estar no formato 'EP-XX', onde XX são dígitos.")
        raise typer.Exit(1)

    if not (status or status_id or subject or description or assigned_to or tags):
        typer.echo(
            "[ERRO] Informe pelo menos um campo para atualizar: --status, --status-id,",
            "--subject, --description, --assigned-to, --tags.",
        )
        raise typer.Exit(1)

    token = ensure_token()
    api_url = get_taiga_api_url()
    api = TaigaAPI(api_url, token)
    service = TaigaService(api)
    try:
        epic = service.get_epic_by_tag_full(epic_tag, int(project_id))
    except ValueError as e:
        typer.echo(f"[ERRO] {e}")
        raise typer.Exit(1)

    payload = {"version": epic["version"]}

    # Resolução do status
    if status_id is not None:
        payload["status"] = status_id
    elif status:
        try:
            payload["status"] = get_epic_status_id_by_name(status)
        except ValueError as e:
            typer.echo(f"[ERRO] {e}")
            raise typer.Exit(1)

    if subject:
        payload["subject"] = subject
    if description:
        payload["description"] = description
    if assigned_to is not None:
        payload["assigned_to"] = assigned_to
    if tags:
        tags_list = [t.strip() for t in tags.split(",") if t.strip()]
        payload["tags"] = tags_list

    # ...
    if not token:
        typer.echo("[ERRO] Token não encontrado. Faça login novamente com 'taiga login'.")
        raise typer.Exit(1)
    try:
        api.patch(f"epics/{epic['id']}", payload)
        typer.echo(f"[OK] Épico {epic_tag} (id={epic['id']}) atualizado com sucesso.")
    except httpx.HTTPStatusError as e:
        typer.echo(f"[ERRO] Falha ao atualizar épico: {e.response.text}")
        raise typer.Exit(1)


@app.command()
def update_initiative(
    initiative_id: str, name: str = typer.Option(None), order: int = typer.Option(None)
):
    """Update an initiative (swimlane) by ID."""
    token = ensure_token()
    api_url = get_taiga_api_url()
    # ...
    if not token:
        typer.echo("[ERRO] Token não encontrado. Faça login novamente com 'taiga login'.")
        raise typer.Exit(1)
    api = TaigaAPI(api_url, token)
    data = {}
    if name:
        data["name"] = name
    if order is not None:
        data["order"] = order
    try:
        api.patch(f"swimlanes/{initiative_id}", data)
        typer.echo(f"[OK] Initiative {initiative_id} updated.")
    except httpx.HTTPStatusError as e:
        typer.echo(f"[ERRO] Falha ao atualizar initiative: {e.response.text}")
        raise typer.Exit(1)
    typer.echo(f"Initiative {initiative_id} updated.")
