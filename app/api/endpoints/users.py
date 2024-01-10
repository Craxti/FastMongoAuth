# app/api/endpoints/users.py

from fastapi import APIRouter, Depends, HTTPException
from fastapi_users import FastAPIUsers, models
from app.models.schemas import User, UserInDB
from app.core.database import database
from app.core.config import settings
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_users.authentication import JWTAuthentication
from fastapi_users.db import TortoiseBaseUserModel
from fastapi_users.models import BaseOAuthAccount, BaseUserDB

router = APIRouter()


fastapi_users = FastAPIUsers(
    User, UserInDB, database,
    models.UserCreate, models.UserUpdate,
    models.UserDB, settings.secret_key
)

jwt_authentication = JWTAuthentication(secret=settings.secret_key)


@router.post("/users/", response_model=User)
async def create_user(user: User):
    user_dict = user.dict()
    user_dict["hashed_password"] = "hashed_password"
    inserted_user = await database.users.insert_one(user_dict)
    return user


@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await fastapi_users.get_user(email=form_data.username)
    if not user or user.hashed_password != "hashed_password":
        raise HTTPException(status_code=401, detail="Incorrect username or password")

    token = jwt_authentication.get_auth_token(models.UserDB(**user), settings.secret_key)
    return {"access_token": token}



@router.get("/current_user")
async def get_current_user(user: models.UserDB = Depends(jwt_authentication)):
    return user

@router.post("/logout")
async def logout(user: models.UserDB = Depends(jwt_authentication)):
    for account in user.oauth_accounts:
        await database.oauth_accounts.delete_one({"account_id": account.id})
    return {"message": "Logged out successfully"}

@router.put("/update_profile")
async def update_profile(user_update: models.UserUpdate, current_user: models.UserDB = Depends(jwt_authentication)):
    updated_user = await database.users.update_one(
        {"id": current_user.id},
        {"$set": user_update.dict(exclude_unset=True)}
    )
    if updated_user.modified_count == 1:
        return {"message": "Profile updated successfully"}
    return {"message": "Profile update failed"}

