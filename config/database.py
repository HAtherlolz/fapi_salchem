# from sqlalchemy.ext.asyncio import create_async_engine
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
import databases
from sqlalchemy import create_engine, MetaData

from .settings import Settings


settings = Settings()

DATABASE_URL = f'postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:5432/{settings.DB_NAME}'

# engine = create_async_engine(DATABASE_URL, echo=True)
# SessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
#
# Base = declarative_base()
database = databases.Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)

metadata = MetaData()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
