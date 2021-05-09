from admin.models.AdmProfile import AdmProfile
from admin.models.AdmPage import AdmPage
from admin.models.AdmUser import AdmUser
import json
from typing import List



class AdmProfileDTO:
    id: int
    administrator: str
    description: str
    general: str
    admPages: List[AdmPage]
    admUsers: List[AdmUser]
    profilePages: str
    profileUsers: str

    def __init__(self, admProfile: AdmProfile):
        self.id = admProfile.id
        self.administrator = admProfile.administrator
        self.description = admProfile.description
        self.general = admProfile.general

    def to_json(self):
        return json.dumps(self.__dict__)
    
    @staticmethod
    def list_to_json(lista: List[AdmProfile]):
        listaDTO = []
        for item in lista:
            dto = AdmProfileDTO(item)
            listaDTO.append(dto.__dict__)
        return json.dumps(listaDTO)