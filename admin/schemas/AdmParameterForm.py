from pydantic import BaseModel, Field
from admin.models.AdmParameter import AdmParameter


class AdmParameterForm(BaseModel):
    code: str
    description: str
    idParameterCategory: int
    value: str
    #admParameterCategory: AdmParameterCategory 

    def to_AdmParameter(self):
        newAdmParameter = AdmParameter(
            code=self.code
            description=self.description
            idParameterCategory=self.idParameterCategory
            value=self.value
            #admParameterCategory=self.admParameterCategory
        )
        return newAdmParameter

    def from_AdmParameter(self, admParameter: AdmParameter):
        admParameter.code=self.code
        admParameter.description=self.description
        admParameter.idParameterCategory=self.idParameterCategory
        admParameter.value=self.value
        #admParameter.admParameterCategory=self.admParameterCategory

        return admParameter
