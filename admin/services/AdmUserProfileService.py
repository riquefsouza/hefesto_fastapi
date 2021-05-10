from fastapi import Depends
from sqlalchemy.orm import Session
from base.database import get_db
from typing import List
from admin.models.AdmUser import AdmUser
from admin.models.AdmProfile import AdmProfile
from admin.models.AdmUserProfile import AdmUserProfile

class AdmUserProfileService:
    def __init__(self):
        pass

    #def setTransient(self, db: Session, plist: List[AdmUserProfile]):
    #    for item in plist:
    #        setTransient(db, item)

    #def setTransient(self, db: Session, item: AdmUserProfile):
    #    item.AdmUser = db.query(AdmUser).filter(AdmUser.id == item.idUser).first()
    #    item.AdmProfile = db.query(AdmProfile).filter(AdmProfile.id == item.idProfile).first()

    def findAll(self, db: Session):
        listAdmUserProfile = db.query(AdmUser).all()
        #self.setTransient(listAdmUserProfile)
        return listAdmUserProfile

    def getProfilesByUser(self, db: Session, admUserId: int):
        listAdmUserProfile = db.query(AdmUserProfile).filter(AdmUserProfile.idUser == admUserId)
        lista = []

        for item in listAdmUserProfile:
            #self.setTransient(item)
            lista.append(item.admProfile)

        return lista

    def getUsersByProfile(self, db: Session, admProfileId: int):
        listAdmUserProfile = db.query(AdmUserProfile).filter(AdmUserProfile.idProfile == admProfileId)
        lista = []

        for item in listAdmUserProfile:
            #self.setTransient(item)
            lista.append(item.admUser)

        return lista