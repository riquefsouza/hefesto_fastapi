from pydantic import BaseModel, Field
from admin.models.AdmParameterCategory import AdmParameterCategory


class AdmParameterCategoryForm(BaseModel):
    description: str
    order: int

    def to_AdmParameterCategory(self):
        newAdmParameterCategory = AdmParameterCategory(
            description=self.description
            order=self.order
        )
        return newAdmParameterCategory

    def from_AdmParameterCategory(self, admParameterCategory: AdmParameterCategory):
        admParameterCategory.description=self.description
        admParameterCategory.order=self.order

        return admParameterCategory
