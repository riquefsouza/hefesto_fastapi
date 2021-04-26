from pydantic import BaseModel, Field
from admin.models.AdmProfile import AdmProfile


class AdmProfileForm(BaseModel):
    administrator: str
    description: str
    general: str

    def to_AdmProfile(self):
        newAdmProfile = AdmProfile(
            administrator=self.administrator,
            description=self.description,
            general=self.general
        )
        return newAdmProfile

    def from_AdmProfile(self, admProfile: AdmProfile):
        admProfile.administrator=self.administrator
        admProfile.description=self.description
        admProfile.general=self.general

        return admProfile
