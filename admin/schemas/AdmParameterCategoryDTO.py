from admin.models.AdmParameterCategory import AdmParameterCategory
import json
from typing import List


class AdmParameterCategoryDTO:
    id: int
    description: str
    order: int

    def __init__(self, admParameterCategory: AdmParameterCategory):
        self.id=admParameterCategory.id
        self.description=admParameterCategory.description
        self.order=admParameterCategory.order

    def to_json(self):
        return json.dumps(self.__dict__)
    
    @staticmethod
    def list_to_json(lista: List[AdmParameterCategory]):
        listaDTO = []
        for item in lista:
            dto = AdmParameterCategoryDTO(item)
            listaDTO.append(dto.__dict__)
        return json.dumps(listaDTO)