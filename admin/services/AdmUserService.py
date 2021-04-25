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
            admUser = form.to_AdmUser()
            db.add(admUser)
            db.commit()
            return admUser
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
                return admUser
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
