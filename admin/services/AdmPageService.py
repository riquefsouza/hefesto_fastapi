from fastapi import Depends
from sqlalchemy.orm import Session
from base.database import get_db
from admin.models.AdmPage import AdmPage
from admin.schemas.AdmPageDTO import AdmPageDTO
from admin.schemas.AdmPageForm import AdmPageForm

class AdmPageService:
    def __init__(self):
        pass

    def findAll(self, db: Session):
        return db.query(AdmPage).all()

    def findById(self, db: Session, id: int):
        return db.query(AdmPage).filter(AdmPage.id == id).first()

    def save(self, db: Session, form: AdmPageForm):
        try:
            admPage = form.to_AdmPage()
            db.add(admPage)
            db.commit()
            return admPage
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
                return admPage
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
