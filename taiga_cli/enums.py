from enum import Enum


class UserStoryStatus(Enum):
    BACKLOG = 14
    READY = 15
    IN_PROGRESS = 16
    REVIEW = 17
    DONE = 18
    ARCHIVED = 19


_USER_STORY_STATUS_NAME_MAP = {
    "backlog": UserStoryStatus.BACKLOG,
    "ready": UserStoryStatus.READY,
    "in progress": UserStoryStatus.IN_PROGRESS,
    "review": UserStoryStatus.REVIEW,
    "done": UserStoryStatus.DONE,
    "archived": UserStoryStatus.ARCHIVED,
}


def get_user_story_status_id_by_name(name: str) -> int:
    key = name.strip().lower().replace("_", " ")
    status = _USER_STORY_STATUS_NAME_MAP.get(key)
    if status:
        return status.value
    raise ValueError(
        f"Status '{name}' não encontrado. Válidos: {', '.join(_USER_STORY_STATUS_NAME_MAP.keys())}"
    )


# Enum estático de status de task para o projeto Hermes Conrad
# Gerado a partir da API /api/v1/task-statuses?project=3
class TaskStatus(Enum):
    NEW = 11
    IN_PROGRESS = 12
    READY_FOR_TEST = 13
    CLOSED = 14
    NEEDS_INFO = 15


_TASK_STATUS_NAME_MAP = {
    "new": TaskStatus.NEW,
    "in progress": TaskStatus.IN_PROGRESS,
    "ready for test": TaskStatus.READY_FOR_TEST,
    "closed": TaskStatus.CLOSED,
    "needs info": TaskStatus.NEEDS_INFO,
}


def get_task_status_id_by_name(name: str) -> int:
    key = name.strip().lower().replace("_", " ")
    status = _TASK_STATUS_NAME_MAP.get(key)
    if status:
        return status.value
    raise ValueError(
        f"Status '{name}' não encontrado. Válidos: {', '.join(_TASK_STATUS_NAME_MAP.keys())}"
    )


# Enum estático de status de épico para o projeto Hermes Conrad
# Gerado a partir da API /api/v1/epic-statuses?project=3


class EpicStatus(Enum):
    NEW = 11
    IN_PROGRESS = 13
    READY = 12
    DONE = 15
    READY_FOR_TEST = 14


_EPIC_STATUS_NAME_MAP = {
    "new": EpicStatus.NEW,
    "in progress": EpicStatus.IN_PROGRESS,
    "ready": EpicStatus.READY,
    "done": EpicStatus.DONE,
    "ready for test": EpicStatus.READY_FOR_TEST,
}


def get_epic_status_id_by_name(name: str) -> int:
    """Retorna o id do status pelo nome (case insensitive, espaços e underscores equivalentes)."""
    key = name.strip().lower().replace("_", " ")
    status = _EPIC_STATUS_NAME_MAP.get(key)
    if status:
        return status.value
    raise ValueError(
        f"Status '{name}' não encontrado. Válidos: {', '.join(_EPIC_STATUS_NAME_MAP.keys())}"
    )
