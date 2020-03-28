from apps.db import Base
from sqlalchemy import Column, Integer, String, Text, text, DATETIME, DATE
from datetime import datetime
import json


class User(Base):
    __tablename__ = "users"
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    username = Column('username', String(32))
    mailaddress = Column('mailaddress', String(255))
    password = Column('password', String(255))
    birthday = Column('birthday', DATE)
    role = Column('role', String(255))
    created_at = Column('created_at', DATETIME, nullable=False, default=datetime.now)
    updated_at = Column('updated_at', DATETIME, nullable=False, default=datetime.now, onupdate=datetime.now)
