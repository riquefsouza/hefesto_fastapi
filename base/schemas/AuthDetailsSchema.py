from pydantic import BaseModel

class AuthDetailsSchema(BaseModel):
	username: str
	password: str
