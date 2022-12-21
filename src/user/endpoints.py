from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status, Request

from . import schemas, crud
from config.settings import Settings
from .jwt_auth import authenticate_user, create_access_token, get_current_active_user


router = APIRouter()
settings = Settings()


@router.post("/users/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate):
    db_user = await crud.get_user_by_email(email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return await crud.create_user(user=user)


@router.get("/users/", response_model=list[schemas.User])
async def users_list(skip: int = 0, limit: int = 100):
    return await crud.get_users(skip=skip, limit=limit)


@router.get("/users/{user_id}", response_model=schemas.User)
async def read_user(user_id: int):
    db_user = await crud.get_user(user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.delete("/users/{user_id}", status_code=204)
async def delete_user(user_id: int):
    db_user = await crud.get_user(user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return await crud.delete_user(user_id=user_id)


@router.post("/auth/user/jwt/", response_model=schemas.Token)
async def login_for_access_token(form_data: schemas.UserCreate = Depends()):
    user = await authenticate_user(form_data.email, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users/me/", response_model=schemas.User)
async def users_me(current_user: schemas.User = Depends(get_current_active_user)):
    return current_user
