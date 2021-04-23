from fastapi import Depends
from sqlalchemy.orm import Session
from base.database import get_db
from admin.models.AdmUser import AdmUser
from admin.schemas.AdmUserDTO import AdmUserDTO

class AdmUserService:
    def __init__(self):
        pass

    def findById(self, db: Session, id: int):
        return db.query(AdmUser).filter(AdmUser.id == id).first()

    def save(self, db: Session, form: AdmUserDTO):
        try:
            newAdmUser = AdmUser(
                active=form.active,
                email=form.email,
                login=form.login,
                name=form.name,
                password=form.password
            )
            db.add(newAdmUser)
            db.commit()
            return newAdmUser
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
