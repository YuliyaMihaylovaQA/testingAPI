from typing import List
from pydantic import BaseModel


class Category(BaseModel):
    id: int
    name: str


class Tags(BaseModel):
    id: int
    name: str


class PetRequestSchema(BaseModel):
    id: int
    name: str
    category: Category
    photoUrls: list[str]
    tags: list[Tags]
    status: str
