from fastapi import Depends
from sqlalchemy.orm import Session
from base.database import get_db
from admin.models.AdmMenu import AdmMenu
from admin.schemas.AdmMenuDTO import AdmMenuDTO
from admin.schemas.AdmMenuForm import AdmMenuForm

class AdmMenuService:
    def __init__(self):
        pass

    def findAll(self, db: Session):
        return db.query(AdmMenu).all()

    def findById(self, db: Session, id: int):
        return db.query(AdmMenu).filter(AdmMenu.id == id).first()

    def save(self, db: Session, form: AdmMenuForm):
        try:
            admMenu = form.to_AdmMenu()
            db.add(admMenu)
            db.commit()
            return admMenu
        except Exception as e:
            print(e)
            db.rollback()
            return None

    def update(self, db: Session, id: int, form: AdmMenuForm):
        try:
            admMenu: AdmMenu = db.query(AdmMenu).get(id)
            if admMenu != None:
                admMenu = form.from_AdmMenu(admMenu)
                db.commit()
                return admMenu
            else:
                return None
        except Exception as e:
            print(e)
            db.rollback()
            return None

    def delete(self, db: Session, id: int):
        try:
            query = db.query(AdmMenu).filter_by(id=id)
            if query.count() > 0:
                db.query(AdmMenu).filter(AdmMenu.id == id).delete()
                db.commit()
                return True
            else:
                return False
        except Exception as e:
            print(e)
            db.rollback()
            return False
    
    def mountMenuItem(self, db: Session, listIdProfile: List[int]):
        pass

