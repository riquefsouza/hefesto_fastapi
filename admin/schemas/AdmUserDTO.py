from admin.models.AdmUser import AdmUser
import json

class AdmUserDTO:
    id: int
    active: str
    email: str
    login: str
    name: str
    password: str

    def __init__(self, admUser: AdmUser):
        self.id = admUser.id
        self.active = admUser.active
        self.email=admUser.email
        self.login=admUser.login
        self.name=admUser.name
        self.password=admUser.assword

    def to_json(self):
        return json.dumps(self.__dict__)
    
