from fastapi import Depends
from sqlalchemy.orm import Session
from base.database import get_db
from admin.models.AdmUser import AdmUser
from admin.schemas.AdmUserDTO import AdmUserDTO
from admin.schemas.AdmUserForm import AdmUserForm
from admin.services.AdmUserProfileService import AdmUserProfileService
from typing import List
import json
#import bcrypt
from passlib.context import CryptContext

class AdmUserService:
    userProfileService = AdmUserProfileService()
    bcrypt = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def __init__(self):
        pass

    def findAll(self, db: Session):
        plist = db.query(AdmUser).all()
        return self.setTransientList(db, plist)

    def findById(self, db: Session, id: int):
        obj = db.query(AdmUser).filter(AdmUser.id == id).first()
        return self.setTransient(db, obj)

    def save(self, db: Session, form: AdmUserForm):
        try:
            admUser = form.to_AdmUser()
            db.add(admUser)
            db.commit()
            return self.setTransient(db, admUser)
        except Exception as e:
            print(e)
            db.rollback()
            return None

    def update(self, db: Session, id: int, form: AdmUserForm):
        try:
            admUser: AdmUser = db.query(AdmUser).get(id)
            if admUser != None:
                admUser = form.from_AdmUser(admUser)
                db.commit()
                return self.setTransient(db, admUser)
            else:
                return None
        except Exception as e:
            print(e)
            db.rollback()
            return None

    def delete(self, db: Session, id: int):
        try:
            query = db.query(AdmUser).filter_by(id=id)
            if query.count() > 0:
                db.query(AdmUser).filter(AdmUser.id == id).delete()
                db.commit()
                return True
            else:
                return False
        except Exception as e:
            print(e)
            db.rollback()
            return False

    def setTransientList(self, db: Session, plist: List[AdmUser]):
        listaDTO = []
        for item in plist:
            dto = self.setTransient(db, item)
            listaDTO.append(dto)
        return listaDTO

    def setTransient(self, db: Session, item: AdmUser):
        dto = AdmUserDTO(item)
        obj = self.userProfileService.getProfilesByUser(db, item.id)
        for profile in obj:
            dto.admIdProfiles.append(profile.id)

        listUserProfiles = []
        for profile in obj:
            listUserProfiles.append(profile.description)
        dto.userProfiles = ",".join(listUserProfiles)
        
        return dto.__dict__

    def authenticate(self, db: Session, login: str, password: str):
        admUser = db.query(AdmUser).filter(AdmUser.login == login).first()

        if admUser != None:
            if self.verifyPassword(password, admUser.password):
                return admUser

        return None

    def verifyPassword(self, password: str, hashPassword: str):
        #return bcrypt.checkpw(password, hashPassword)
        return self.bcrypt.verify(password, hashPassword)

    def register(self, model: AdmUser):
        #hash = bcrypt.hashpw(model.password.encode('utf8'), bcrypt.gensalt(10))
        hash = self.bcrypt.hash(model.password.encode('utf8'))
        model.password = hash
