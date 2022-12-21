from datetime import datetime
from pydantic import BaseModel

from src.units.schemas import Unit


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool = False
    date_created: datetime | None
    nickname: str | None
    units: list[Unit] = []

    class Config:
        orm_mode = True
