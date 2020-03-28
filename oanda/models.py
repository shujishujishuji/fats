from apps.db import Base, engine
from sqlalchemy import Column, CHAR, VARCHAR, ForeignKey


class Oanda(Base):
    __tablename__ = "oanda"
    id = Column(
        'id',
        CHAR(20),
        ForeignKey('users.id'),
        nullable=False,
        primary_key=True,
        autoincrement=False,
        unique=True)
    token = Column(
        'token',
        VARCHAR(255),
        nullable=False)
