from apps.db import Base
from sqlalchemy import Column, VARCHAR, DATETIME, CHAR, BOOLEAN
from sqlalchemy.orm import relationship
from datetime import datetime


class User(Base):
    __tablename__ = "users"
    id = Column(
        'id',
        CHAR(20),
        nullable=False,
        primary_key=True,
        autoincrement=False,
        unique=True)
    username = Column('username', VARCHAR(255), nullable=False, unique=True)
    mailaddress = Column('mailaddress', VARCHAR(255))
    password = Column('password', VARCHAR(255), nullable=False)
    delete_flag = Column(
        'delete_flag',
        BOOLEAN,
        nullable=False,
        default=False)
    created_at = Column(
        'created_at',
        DATETIME,
        nullable=False,
        default=datetime.now)
    updated_at = Column(
        'updated_at',
        DATETIME,
        nullable=False,
        default=datetime.now,
        onupdate=datetime.now)
    userconfig = relationship('UserConfig', backref='users', lazy=True)
    oanda = relationship('Oanda', backref='users', lazy=True)
