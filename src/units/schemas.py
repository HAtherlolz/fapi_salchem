from typing import Union

from pydantic import BaseModel


class UnitBase(BaseModel):
    title: str
    description: Union[str, None] = None


class UnitCreate(UnitBase):
    pass


class Unit(UnitBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
