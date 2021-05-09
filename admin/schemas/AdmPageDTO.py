from admin.models.AdmPage import AdmPage
import json
from typing import List


class AdmPageDTO:
    id: int
    description: str
    url: str
    admIdProfiles: List[int]
    pageProfiles: str

    def __init__(self, admPage: AdmPage):
        self.id = admPage.id
        self.description = admPage.description
        self.url = admPage.url
        self.admIdProfiles = []
        self.pageProfiles = ""

    def to_json(self):
        #return json.dumps(self.__dict__)
        return self.__dict__
    
    @staticmethod
    def list_to_json(lista: List[AdmPage]):
        listaDTO = []
        for item in lista:
            dto = AdmPageDTO(item)
            listaDTO.append(dto.__dict__)
        #return json.dumps(listaDTO)
        return listaDTO