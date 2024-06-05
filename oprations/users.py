from xml.dom import ValidationErr

import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession

from db.models import User


class UserOprations:
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session

    async def create(self, username: str, password: str) -> User:
        user = User(password=password, username=username)
        async with self.db_session as session:
            session.add(user)
            await session.commit()
        return user

    async def get_user_by_username(self, username: str) -> User:
        query = sa.select(User).where(User.username == username)
        async with self.db_session as session:
            user_data = await session.scalar(query)
            if user_data is None:
                raise ValidationErr('User non found')
            return user_data
