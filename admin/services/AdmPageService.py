from fastapi import Depends
from sqlalchemy.orm import Session
from base.database import get_db
from admin.models.AdmPage import AdmPage
from admin.schemas.AdmPageDTO import AdmPageDTO
from admin.schemas.AdmPageForm import AdmPageForm
from admin.services.AdmPageProfileService import AdmPageProfileService
from typing import List
import json

class AdmPageService:
    pageProfileService = AdmPageProfileService()

    def __init__(self):
        pass

    def findAll(self, db: Session):
        plist = db.query(AdmPage).all()
        return self.setTransientList(db, plist)

    def findById(self, db: Session, id: int):
        obj = db.query(AdmPage).filter(AdmPage.id == id).first()
        return self.setTransient(db, obj)

    def save(self, db: Session, form: AdmPageForm):
        try:
            admPage = form.to_AdmPage()
            db.add(admPage)
            db.commit()
            return self.setTransient(db, admPage)
        except Exception as e:
            print(e)
            db.rollback()
            return None

    def update(self, db: Session, id: int, form: AdmPageForm):
        try:
            admPage: AdmPage = db.query(AdmPage).get(id)
            if admPage != None:
                admPage = form.from_AdmPage(admPage)
                db.commit()
                return self.setTransient(db, admPage)
            else:
                return None
        except Exception as e:
            print(e)
            db.rollback()
            return None

    def delete(self, db: Session, id: int):
        try:
            query = db.query(AdmPage).filter_by(id=id)
            if query.count() > 0:
                db.query(AdmPage).filter(AdmPage.id == id).delete()
                db.commit()
                return True
            else:
                return False
        except Exception as e:
            print(e)
            db.rollback()
            return False

    def setTransientList(self, db: Session, plist: List[AdmPage]):
        listaDTO = []
        for item in plist:
            dto = self.setTransient(db, item)
            listaDTO.append(dto)
        return listaDTO

    def setTransient(self, db: Session, item: AdmPage):
        dto = AdmPageDTO(item)
        obj = self.pageProfileService.getProfilesByPage(db, item.id)
        for profile in obj:
            dto.admIdProfiles.append(profile.id)

        listPageProfiles = []
        for profile in obj:
            listPageProfiles.append(profile.description)
        dto.pageProfiles = ",".join(listPageProfiles)
        
        return dto.__dict__

