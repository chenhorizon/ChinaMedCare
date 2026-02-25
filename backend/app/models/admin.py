from pydantic import BaseModel


class AdminLogin(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    username: str | None = None


class AdminResponse(BaseModel):
    username: str
    message: str = "Login successful"
