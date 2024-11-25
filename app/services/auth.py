from sqlalchemy.orm import Session
from app.models.users import Users
from app.utils.hash import hash_password, verify_password
from app.utils.jwt import create_access_token

def create_user(db: Session, username: str, email: str, password: str):
    hashed_pw = hash_password(password)
    user = Users(username=username, email=email, hashed_password=hashed_pw)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(Users).filter(Users.username == username).first()
    if not user or not verify_password(password, user.hashed_password):
        return None
    return create_access_token(data={"sub": user.username})
