from fastapi import Depends
from sqlalchemy.orm import Session
from base.database import get_db
from admin.models.AdmProfile import AdmProfile
from admin.schemas.AdmProfileDTO import AdmProfileDTO
from admin.schemas.AdmPageDTO import AdmPageDTO
from admin.schemas.AdmUserDTO import AdmUserDTO
from admin.schemas.AdmProfileForm import AdmProfileForm
from admin.services.AdmPageProfileService import AdmPageProfileService
from admin.services.AdmUserProfileService import AdmUserProfileService
from typing import List
import json

class AdmProfileService:
    pageProfileService = AdmPageProfileService()
    userProfileService = AdmUserProfileService()

    def __init__(self):
        pass

    def findAll(self, db: Session):
        plist = db.query(AdmProfile).all()
        return self.setTransientList(db, plist)

    def findById(self, db: Session, id: int):
        obj = db.query(AdmProfile).filter(AdmProfile.id == id).first()
        return self.setTransient(db, obj)

    def save(self, db: Session, form: AdmProfileForm):
        try:
            admProfile = form.to_AdmProfile()
            db.add(admProfile)
            db.commit()
            return self.setTransient(db, admProfile)
        except Exception as e:
            print(e)
            db.rollback()
            return None

    def update(self, db: Session, id: int, form: AdmProfileForm):
        try:
            admProfile: AdmProfile = db.query(AdmProfile).get(id)
            if admProfile != None:
                admProfile = form.from_AdmProfile(admProfile)
                db.commit()
                return self.setTransient(db, admProfile)
            else:
                return None
        except Exception as e:
            print(e)
            db.rollback()
            return None

    def delete(self, db: Session, id: int):
        try:
            query = db.query(AdmProfile).filter_by(id=id)
            if query.count() > 0:
                db.query(AdmProfile).filter(AdmProfile.id == id).delete()
                db.commit()
                return True
            else:
                return False
        except Exception as e:
            print(e)
            db.rollback()
            return False

    def setTransientList(self, db: Session, plist: List[AdmProfile]):
        listaDTO = []
        for item in plist:
            dto = self.setTransient(db, item)
            listaDTO.append(dto)
        return listaDTO

    def setTransient(self, db: Session, item: AdmProfile):
        dto = AdmProfileDTO(item)
        obj = self.pageProfileService.getPagesByProfile(db, item.id)
        for page in obj:
            pageDTO = AdmPageDTO(page)
            dto.admPages.append(pageDTO.__dict__)

        listProfilePages = []
        for page in obj:
            listProfilePages.append(page.description)
        dto.profilePages = ",".join(listProfilePages)

        obj = self.userProfileService.getUsersByProfile(db, item.id)
        for user in obj:
            userDTO = AdmUserDTO(user)
            dto.admUsers.append(userDTO.__dict__)

        listProfileUsers = []
        for user in obj:
            listProfileUsers.append(user.name)
        dto.profileUsers = ",".join(listProfileUsers)

        return dto.__dict__

    def findProfilesByPage(self, db: Session, pageId: int):
        return self.pageProfileService.getProfilesByPage(db, pageId)

    def findProfilesByUser(self, db: Session, userId: int):
        return self.userProfileService.getProfilesByUser(db, userId)
    