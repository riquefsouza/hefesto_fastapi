from pydantic import BaseModel, Field
from admin.models.AdmUser import AdmUser


class AdmUserForm(BaseModel):
    email: str = Field(..., example = "example@email.com")
    login: str
    name: str
    password: str
    active: str
    
    def to_AdmUser(self):
        newAdmUser = AdmUser(
            active=self.active,
            email=self.email,
            login=self.login,
            name=self.name,
            password=self.password
        )
        return newAdmUser

    def from_AdmUser(self, admUser: AdmUser):
        admUser.active = self.active
        admUser.email=self.email
        admUser.login=self.login
        admUser.name=self.name
        admUser.password=self.password

        return admUser
        