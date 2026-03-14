from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Task:
    id: str
    subject: str
    status: str
    story_id: Optional[str] = None
    tags: List[str] = field(default_factory=list)


@dataclass
class Story:
    id: str
    subject: str
    status: str
    epic_id: Optional[str] = None
    tags: List[str] = field(default_factory=list)


@dataclass
class Epic:
    id: str
    subject: str
    status: str
    initiative: Optional[str] = None
    tags: List[str] = field(default_factory=list)


@dataclass
class Initiative:
    id: str
    name: str
    order: int
