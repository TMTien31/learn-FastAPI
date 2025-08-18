from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, database, models
from ..hashing import Hash

router = APIRouter(
  tags=['Authentication'],
)

@router.post('/login')
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
  user = db.query(models.User).filter(models.User.email == request.username).first()
  if not user:
    raise HTTPException(status_code=400, detail="Invalid credentials")
  if not Hash.verify(user.password, request.password):
    return HTTPException(status_code=400, detail="Incorrect password")
  #generate a jwt token and return 
  return user