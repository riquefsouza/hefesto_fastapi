from pydantic import BaseModel, Field
from admin.models.AdmPage import AdmPage


class AdmPageForm(BaseModel):
    description: str
    url: str

    def to_AdmPage(self):
        newAdmPage = AdmPage(
            description=self.description
            url=self.url
        )
        return newAdmPage

    def from_AdmPage(self, admPage: AdmPage):
        admPage.description=self.description
        admPage.url=self.url

        return admPage
