from __future__ import annotations
from pydantic import BaseModel

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    is_active: bool

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

class Apple(BaseModel):
    editor: str
