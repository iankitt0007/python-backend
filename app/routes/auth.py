from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.users import Users
from app.utils.hash import verify_password, hash_password
from app.utils.jwt import create_access_token
from app.database import get_session

router = APIRouter()

@router.post("/signup")
async def signup(username: str, email: str, password: str, session: AsyncSession = Depends(get_session)):
    hashed_pw = hash_password(password)
    new_user = Users(username=username, email=email, hashed_password=hashed_pw)
    session.add(new_user)
    await session.commit()
    return {"message": "User created successfully"}

@router.post("/login")
async def login(email: str, password: str, session: AsyncSession = Depends(get_session)):
    user = await session.execute(f"SELECT * FROM users WHERE email = :email", {"email": email})
    user = user.fetchone()
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}
