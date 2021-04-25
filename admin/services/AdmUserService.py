from fastapi import Depends
from sqlalchemy.orm import Session
from base.database import get_db
from admin.models.AdmUser import AdmUser
from admin.schemas.AdmUserDTO import AdmUserDTO
from admin.schemas.AdmUserForm import AdmUserForm

class AdmUserService:
    def __init__(self):
        pass

    def findAll(self, db: Session):
        return db.query(AdmUser).all()

    def findById(self, db: Session, id: int):
        return db.query(AdmUser).filter(AdmUser.id == id).first()

    def save(self, db: Session, form: AdmUserForm):
        try:
            newAdmUser = form.to_AdmUser()
            db.add(newAdmUser)
            db.commit()
            return newAdmUser
        except Exception as e:
            print(e)
            db.rollback()
            return Null

    def update(self, db: Session, id: int, form: AdmUserForm):
        try:
            admUser: AdmUser = db.query(AdmUser).get(id)
            admUser = form.from_AdmUser(admUser)
            db.commit()
            return admUser
        except Exception as e:
            print(e)
            db.rollback()
            return Null

    def delete(self, db: Session, id: int):
        try:
            db.query(AdmUser).filter(AdmUser.id == id).delete()
            db.commit()
            return True
        except Exception as e:
            print(e)
            db.rollback()
            return False
