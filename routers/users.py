from typing import Annotated
from xml.dom import UserDataHandler

from fastapi import APIRouter, Body, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.engins import get_db
from oprations.users import UserOprations
from schema._input import RegisterInput, UpdataUserUsernameInput

router = APIRouter()


@router.post("/register")
async def register(
    db_session: Annotated[AsyncSession, Depends(get_db)],
    data: RegisterInput = Body()
):
    user = await UserOprations(db_session).create(
        username=data.username, password=data.password
    )
    return user


@router.post("/login")
async def login(): ...


@router.get("/{username}/")
async def get_user_profile(
    db_session: Annotated[AsyncSession, Depends(get_db)], username: str
):
    profile = await UserOprations(db_session).get_user_by_username(username)
    return profile


@router.put("/")
async def user_update_profile(
    db_session: Annotated[AsyncSession, Depends(get_db)],
    data: UpdataUserUsernameInput = Body()
):
    user = await UserOprations(db_session).update_username(data.old_username, data.new_username)
    return user
