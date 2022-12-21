from datetime import datetime

from fastapi import status

from . import models, schemas
from .jwt_auth import get_password_hash
from config.database import database


async def get_user(user_id: int):
    user = dict(await database.fetch_one(models.users.select().where(models.users.c.id == user_id)))
    return user


async def get_user_by_email(email: str):
    return await database.fetch_one(models.users.select().where(models.users.c.email == email))


async def get_users(skip: int = 0, limit: int = 100):
    results = await database.fetch_all(models.users.select().offset(skip).limit(limit))
    return [dict(result) for result in results]


async def create_user(user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    time_now = datetime.utcnow()
    db_user = models.users.insert().values(email=user.email, password=hashed_password, date_created=time_now)
    user_id = await database.execute(db_user)
    return schemas.User(**user.dict(), id=user_id)


async def delete_user(user_id: int):
    db_user = models.users.delete().where(models.users.c.id == user_id)
    await database.execute(db_user)
    return status.HTTP_204_NO_CONTENT
