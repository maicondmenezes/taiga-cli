from typing import List

from .api import TaigaAPI
from .models import Epic, Initiative, Story, Task


class TaigaService:
    def get_story_by_tag_full(self, tag: str, project_id: int) -> dict:
        """
        Busca o dict completo do primeiro user story do projeto que contenha a tag (case insensitive) na lista de tags.
        Retorna o dict do story (com id, version, etc).
        """
        tag_norm = tag.lower()
        data = self.api.get("userstories", {"project": project_id})
        for s in data:
            tags = [t[0].lower() for t in s.get("tags", []) if t and t[0]]
            if tag_norm in tags:
                return s
        raise ValueError(f"Nenhum user story com a tag '{tag}' encontrado no projeto {project_id}.")

    def get_epic_by_tag_full(self, tag: str, project_id: int) -> dict:
        """
        Busca o dict completo do primeiro épico do projeto que contenha a tag (case insensitive) na lista de tags.
        Retorna o dict do épico (com id, version, etc).
        """
        tag_norm = tag.lower()
        data = self.api.get("epics", {"project": project_id})
        for e in data:
            tags = [t[0].lower() for t in e.get("tags", []) if t and t[0]]
            if tag_norm in tags:
                return e
        raise ValueError(f"Nenhum épico com a tag '{tag}' encontrado no projeto {project_id}.")

    def get_epic_id_by_tag(self, tag: str, project_id: int) -> str:
        """
        Busca o id do primeiro épico do projeto que contenha a tag (case insensitive) na lista de tags.
        """
        tag_norm = tag.lower()
        epics = self.list_epics(project_id)
        for epic in epics:
            tags = getattr(epic, "tags", [])
            if tag_norm in tags:
                return epic.id
        raise ValueError(f"Nenhum épico com a tag '{tag}' encontrado no projeto {project_id}.")

    def __init__(self, api: TaigaAPI):
        self.api = api

    def list_tasks(self, project_id: int) -> List[Task]:
        data = self.api.get("tasks", {"project": project_id})
        return [Task(id=str(t["id"]), subject=t["subject"], status=t["status"]) for t in data]

    def list_stories(self, project_id: int) -> List[Story]:
        data = self.api.get("userstories", {"project": project_id})
        return [Story(id=str(s["id"]), subject=s["subject"], status=s["status"]) for s in data]

    def list_epics(self, project_id: int) -> List[Epic]:
        data = self.api.get("epics", {"project": project_id})
        return [
            Epic(id=str(e["id"]), subject=e["subject"], status=e["status"], tags=[t[0] for t in e.get("tags", [])])
            for e in data
        ]

    def list_initiatives(self, project_id: int) -> List[Initiative]:
        data = self.api.get(f"projects/{project_id}")["swimlanes"]
        return [Initiative(id=str(i["id"]), name=i["name"], order=i["order"]) for i in data]
