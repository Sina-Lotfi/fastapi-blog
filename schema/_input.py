from pydantic import BaseModel


class RegisterInput(BaseModel):
    username: str
    password: str


class UpdataUserUsernameInput(BaseModel):
    old_username: str
    new_username: str


class UserDeleteProfileInput(BaseModel):
    username: str
    password: str
