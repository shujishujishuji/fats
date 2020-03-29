from apps.db import Base
from sqlalchemy import Column, CHAR, BOOLEAN, ForeignKey


class UserConfig(Base):
    __tablename__ = "userconfig"
    id = Column(
        'id',
        CHAR(20),
        ForeignKey('users.id'),
        nullable=False,
        primary_key=True,
        autoincrement=False,
        unique=True)
    symbol = Column('symbol', CHAR(7))
    switch = Column(
        'auto tradeing switch',
        BOOLEAN,
        nullable=False,
        default=False)
