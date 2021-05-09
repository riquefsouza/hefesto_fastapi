from admin.models.AdmUser import AdmUser
import json
from typing import List

class AdmUserDTO:
    id: int
    active: str
    email: str
    login: str
    name: str
    password: str
    admIdProfiles: List[int]
    userProfiles: str
    currentPassword: str
    newPassword: str
    confirmNewPassword: str

    def __init__(self, admUser: AdmUser):
        self.id = admUser.id
        self.active = admUser.active
        self.email=admUser.email
        self.login=admUser.login
        self.name=admUser.name
        self.password=admUser.password

    def to_json(self):
        return json.dumps(self.__dict__)
    
    @staticmethod
    def list_to_json(lista: List[AdmUser]):
        listaDTO = []
        for item in lista:
            dto = AdmUserDTO(item)
            listaDTO.append(dto.__dict__)
        return json.dumps(listaDTO)