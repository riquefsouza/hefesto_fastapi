from pydantic import BaseModel, Field
from admin.models.AdmUser import AdmUser


class AdmMenuForm(BaseModel):
    description: str
    idMenuParent: int
    idPage: int
    order: int
    #admMenuParent
    #admPage

    def to_AdmMenu(self):
        newAdmMenu = AdmMenu(
            description=self.description
            idMenuParent=self.idMenuParent
            idPage=self.idPage
            order=self.order
        )
        return newAdmMenu

    def from_AdmMenu(self, admMenu: AdmMenu):
        admMenu.description=self.description
        admMenu.idMenuParent=self.idMenuParent
        admMenu.idPage=self.idPage
        admMenu.order=self.order

        return admMenu
