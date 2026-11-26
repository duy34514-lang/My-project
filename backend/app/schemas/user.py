from pydantic import BaseModel, ConfigDict


class UserCreat(BaseModel):
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class UserEsponse(BaseModel):
    id: int
    email: str
    username: str
    role: str

    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
