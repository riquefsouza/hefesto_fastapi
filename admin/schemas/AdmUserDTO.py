from pydantic import BaseModel

class AdmUserDTO(BaseModel):
    email: str
    login: str
    name: str
    password: str
    active: str
