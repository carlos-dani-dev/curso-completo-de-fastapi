from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Path
from starlette import status
from ..database import SessionLocal
from pydantic import BaseModel, Field
from ..models import Todos, Users
from .auth import get_current_user
from passlib.context import CryptContext


router = APIRouter(
    prefix='/user',
    tags=['user']
)


def get_db():
    """
    Abre uma nova conexão com o banco de dados e a retorna (yield)
    Após o fim do escopo em que a função get_db é chamada, a conexão é fechada
    """

    db = SessionLocal()
    try: yield db
    finally: db.close()


db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


class UserVerification(BaseModel):
    password: str
    new_password: str

@router.get('/', status_code=status.HTTP_200_OK)
async def get_user_info(user: user_dependency, db: db_dependency):
    if user is None: raise HTTPException(status_code=401, detail='Authentication Failed')
    user_model = db.query(Users).filter(Users.id == user.get('id')).first()
    return user_model


@router.put('/password', status_code=status.HTTP_204_NO_CONTENT)
async def change_password(user: user_dependency, db: db_dependency, user_verification: UserVerification):
    if user is None: raise HTTPException(status_code=401, detail='Authentication Failed')
    user_model = db.query(Users).filter(Users.id == user.get('id')).first()
    
    if not bcrypt_context.verify(user_model.hashed_password, user_verification.password):
        raise HTTPException(status_code=401, detail='Error on password change')
    
    user_model.hashed_password = bcrypt_context.hash(user_verification.password)
    db.add(user_model)
    db.commit()


@router.put('/phonenumber/{phone_number}', status_code=status.HTTP_204_NO_CONTENT)
async def change_phone_number(user: user_dependency, db: db_dependency, phone_number: str = Path(min_length=8)):
    if user is None: raise HTTPException(status_code=401, detail='Authentication Failed')
    user_model = db.query(Users).filter(Users.id == user.get('id')).first()
    
    user_model.phone_number = phone_number
    db.add(user_model)
    db.commit()