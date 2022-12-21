from typing import Union

from pydantic import BaseModel

from src.units.schemas import Unit


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    units: list[Unit] = []

    class Config:
        orm_mode = True
