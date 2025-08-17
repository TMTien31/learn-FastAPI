from pydantic import BaseModel
from typing import List, Optional

class Blog(BaseModel):
    title: str
    body: str

class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str


class ShowBlog(BaseModel):
    title: str
    body: str
  
