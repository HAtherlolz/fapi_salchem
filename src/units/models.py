from sqlalchemy import Table, Column, ForeignKey, Integer, String

from config.database import engine, metadata



units = Table(
    'units',
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("title", String, index=True),
    Column("description", String, index=True),
    Column("owner_id", ForeignKey("users.id")),
)
# class Unit(Base):
#     __tablename__ = 'units'
#
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     description = Column(String, index=True)
#     owner_id = Column(Integer, ForeignKey("users.id", ondelete='CASCADE'))
#     owner = relationship("models.User", back_populates="units")
