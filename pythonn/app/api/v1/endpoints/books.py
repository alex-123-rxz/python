from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
from app.core.deps import get_current_user
from app.db.session import get_session
from app.models.book import Book, BookCreate, BookUpdate
from app.models.user import User

router = APIRouter()

@router.post("/", response_model=Book)
def create_book(
    book: BookCreate,
    db: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@router.get("/", response_model=List[Book])
def read_books(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    books = db.exec(select(Book).offset(skip).limit(limit)).all()
    return books

@router.get("/{book_id}", response_model=Book)
def read_book(
    book_id: int,
    db: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    book = db.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.patch("/{book_id}", response_model=Book)
def update_book(
    book_id: int,
    book_update: BookUpdate,
    db: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    db_book = db.get(Book, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    update_data = book_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_book, field, value)
    
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book