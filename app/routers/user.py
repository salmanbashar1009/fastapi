from fastapi import FastAPI, HTTPException, status, Depends, APIRouter
from .. import models, schemas, utils
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter()



# ======================================
# create user
@router.post('/user/create', status_code=status.HTTP_201_CREATED, response_model=schemas.UserRes)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail= 'Email already exists'
        )

    hashed_password = utils.hash_password(user.password)
    user.password = hashed_password
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# get all users
@router.get("/users", response_model=list[schemas.UserRes])
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

