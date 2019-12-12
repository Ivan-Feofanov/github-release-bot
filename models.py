from datetime import datetime
from enum import Enum

from pydantic import BaseModel, HttpUrl


class Actions(str, Enum):
    published = 'published'
    unpublished = 'unpublished'
    created = 'created'
    edited = 'edited'
    deleted = 'deleted'
    released = 'released'
    prereleased = 'prereleased'


class Repository(BaseModel):
    name: str


class Author(BaseModel):
    login: str
    avatar_url: HttpUrl


class Release(BaseModel):
    name: str
    draft: bool = False
    tag_name: str
    html_url: HttpUrl
    author: Author
    created_at: datetime
    published_at: datetime = None
    body: str


class Body(BaseModel):
    action: str
    release: Release
    repository: Repository
