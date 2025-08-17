from typing import List
from fastapi import APIRouter, Depends
from .. import schemas, models, database
from ..database import SessionLocal
from sqlalchemy.orm import Session, joinedload
from .. import schemas, models, database
from ..database import SessionLocal
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/blog", response_model=List[schemas.ShowBlog], tags=["blogs"])
def all(db: Session = Depends(database.get_db)):
    blogs = db.query(models.Blog).options(models.joinedload(models.Blog.creator)).all()
    return blogs