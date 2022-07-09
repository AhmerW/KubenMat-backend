from fastapi import APIRouter, Request

from fastapi.param_functions import Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from app.auth.firebase import UserRecord, verify_user

from app.models import ValueModel
from app.responses import BaseResponse, Error


router = APIRouter()


async def get_current_user(request: Request) -> UserRecord:
    token = request.headers.get("Authorization")
    if token is None:
        raise Error("Invalid credentials")

    return await verify_user(token)


async def get_admin(request: Request) -> UserRecord:
    user = await get_current_user(request)
    if not user.admin:
        raise Error("Invalid credentials")

    return user
