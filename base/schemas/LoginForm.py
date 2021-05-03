from pydantic import BaseModel

class LoginForm(BaseModel):
    login: str
    password: str
