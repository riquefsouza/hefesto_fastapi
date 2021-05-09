from fastapi import Depends
from sqlalchemy.orm import Session
from base.database import get_db
from typing import List
from admin.models.AdmPage import AdmPage
from admin.models.AdmProfile import AdmProfile
from admin.models.AdmPageProfile import AdmPageProfile


class AdmPageProfileService:
    def __init__(self):
        pass

    #def setTransient(self, db: Session, list: List[AdmPageProfile]):
    #    for item in list:
    #        setTransient(db, item)

    #def setTransient(self, db: Session, item: AdmPageProfile):
    #    item.AdmPage = db.query(AdmPage).filter(AdmPage.id == item.idPage).first()
    #    item.AdmProfile = db.query(AdmProfile).filter(AdmProfile.id == item.idProfile).first()

    def findAll(self, db: Session):
        listAdmPageProfile = db.query(AdmPage).all()
        #self.setTransient(listAdmPageProfile)
        return listAdmPageProfile

    def getProfilesByPage(self, db: Session, admPageId: int):
        listAdmPageProfile = db.query(AdmPageProfile).filter_by(idPage = admPageId).all()
        lista = []

        for item in listAdmPageProfile:
            #self.setTransient(item)
            lista.append(item.admProfile)

        return lista

    def getPagesByProfile(self, db: Session, admProfileId: int):
        listAdmPageProfile = db.query(AdmPageProfile).filter_by(idProfile = admProfileId).all()
        lista = []

        for item in listAdmPageProfile:
            #self.setTransient(item)
            lista.append(item.admPage)

        return lista