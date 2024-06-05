from typing import Annotated

from fastapi import APIRouter, Body, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.engins import get_db
from oprations.users import UserOprations
from schema._input import RegisterInput, UpdataUserUsernameInput, UserDeleteProfileInput

router = APIRouter()


@router.post("/register")
async def register(
    db_session: Annotated[AsyncSession, Depends(get_db)], data: RegisterInput = Body()
):
    user = await UserOprations(db_session).create(
        username=data.username, password=data.password
    )
    return user


@router.get("/{username}/")
async def get_user_profile(
    db_session: Annotated[AsyncSession, Depends(get_db)], username: str
):
    profile = await UserOprations(db_session).get_user_by_username(username)
    return profile


@router.put("/")
async def user_update_profile(
    db_session: Annotated[AsyncSession, Depends(get_db)],
    data: UpdataUserUsernameInput = Body(),
):
    user = await UserOprations(db_session).update_username(
        data.old_username, data.new_username
    )
    return user


@router.delete("/")
async def delete_user_profile(
    db_session: Annotated[AsyncSession, Depends(get_db)],
    data: UserDeleteProfileInput = Body(),
):
    await UserOprations(db_session).user_delete_account(
        username=data.username, password=data.password
    )
