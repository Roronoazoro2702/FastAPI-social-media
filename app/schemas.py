from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional
# from pydantic.types import conint


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class Userout(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True


class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: Userout

    class Config:
        from_attributes = True


class PostOut(PostBase):
    Post: Post
    votes: int
    title: Optional[str] = None  # Mark title as optional
    content: Optional[str] = None  # Mark content as optional

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class Userlogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: str


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)  # type: ignore
