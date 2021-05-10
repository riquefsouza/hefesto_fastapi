from admin.models.AdmMenu import AdmMenu
from admin.models.AdmPage import AdmPage
from admin.schemas.AdmPageDTO import AdmPageDTO
import json
from typing import List


class AdmMenuDTO:
    id: int
    description: str
    idMenuParent: int
    idPage: int
    order: int
    #admMenuParent: AdmMenuDTO
    admPage: AdmPageDTO
    url: str
    subMenus = []

    def __init__(self, admMenu: AdmMenu):
        if admMenu!=None:
            self.id = admMenu.id
            self.description = admMenu.description
            self.idMenuParent = admMenu.idMenuParent
            self.idPage = admMenu.idPage
            self.order = admMenu.order
            #self.admMenuParent = AdmMenuDTO(admMenu.admMenuParent)
            #self.admPage = AdmPageDTO(admMenu.admPage)
            self.url = ""
            self.subMenus = []

    def to_json(self):
        return json.dumps(self.__dict__)
    
    @staticmethod
    def list_to_json(lista: List[AdmMenu]):
        listaDTO = []
        for item in lista:
            dto = AdmMenuDTO(item)
            listaDTO.append(dto.__dict__)
        return json.dumps(listaDTO)