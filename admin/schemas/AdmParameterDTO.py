from admin.models.AdmParameter import AdmParameter
from admin.schemas.AdmParameterCategoryDTO import AdmParameterCategoryDTO
import json
from typing import List


class AdmParameterDTO:
    id: int
    code: str
    description: str
    idParameterCategory: int
    value: str
    admParameterCategory: AdmParameterCategoryDTO

    def __init__(self, admParameter: AdmParameter):
        self.id = admParameter.id
        self.code = admParameter.code
        self.description = admParameter.description
        self.idParameterCategory = admParameter.idParameterCategory
        self.value = admParameter.value
        #self.admParameterCategory = AdmParameterCategoryDTO()

    def to_json(self):
        return json.dumps(self.__dict__)
    
    @staticmethod
    def list_to_json(lista: List[AdmParameter]):
        listaDTO = []
        for item in lista:
            dto = AdmParameterDTO(item)
            listaDTO.append(dto.__dict__)
        return json.dumps(listaDTO)