from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class BookBase(SQLModel):
    title: str
    author: str
    description: Optional[str] = None
    isbn: str = Field(unique=True, index=True)
    published_year: int

class Book(BookBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class BookCreate(BookBase):
    pass

class BookUpdate(SQLModel):
    title: Optional[str] = None
    author: Optional[str] = None
    description: Optional[str] = None
    published_year: Optional[int] = None