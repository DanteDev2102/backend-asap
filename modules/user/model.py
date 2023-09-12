from db import BaseModel
from sqlalchemy import Column, String, Boolean, Integer, Enum
from pydantic import BaseModel as Base
import enum


class ERol(enum.Enum):
    logistic = "L"
    production_control = "PC"
    seller = "V"
    user = "U"
    admin = "A"


class UserModel(Base):
    id: int | None = None
    name: str
    lastname: str
    active: bool | None = None
    code: str
    password: str
    role: ERol


class LoginModel(Base):
    code: str
    password: str


class User(BaseModel):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(60))
    lastname = Column(String(80))
    active = Column(Boolean, default=True)
    code = Column(String(10))
    password = Column(String(120))
    role = Column(Enum(ERol))
