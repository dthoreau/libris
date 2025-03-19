from pydantic import BaseModel, UUID4


class UserBase(BaseModel):
    username: str
    email: str
    full_name: str
    disabled: bool


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: UUID4
