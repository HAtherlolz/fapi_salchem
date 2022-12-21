from datetime import datetime

from sqlalchemy import Table, Boolean, Column, Integer, String, DateTime

from config.database import engine, metadata


users = Table(
    'users',
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("email", String, unique=True, index=True),
    Column("nickname", String),
    Column("password", String),
    Column("is_active", Boolean, default=False),
    Column("date_created", DateTime, default=datetime.utcnow)
)


