from fastapi import Depends
from sqlalchemy.orm import Session
from base.database import get_db
from admin.models.AdmParameter import AdmParameter
from admin.schemas.AdmParameterDTO import AdmParameterDTO
from admin.schemas.AdmParameterForm import AdmParameterForm

class AdmParameterService:
    def __init__(self):
        pass

    def findAll(self, db: Session):
        return db.query(AdmParameter).all()

    def findById(self, db: Session, id: int):
        return db.query(AdmParameter).filter(AdmParameter.id == id).first()

    def save(self, db: Session, form: AdmParameterForm):
        try:
            admParameter = form.to_AdmParameter()
            db.add(admParameter)
            db.commit()
            return admParameter
        except Exception as e:
            print(e)
            db.rollback()
            return None

    def update(self, db: Session, id: int, form: AdmParameterForm):
        try:
            admParameter: AdmParameter = db.query(AdmParameter).get(id)
            if admParameter != None:
                admParameter = form.from_AdmParameter(admParameter)
                db.commit()
                return admParameter
            else:
                return None
        except Exception as e:
            print(e)
            db.rollback()
            return None

    def delete(self, db: Session, id: int):
        try:
            query = db.query(AdmParameter).filter_by(id=id)
            if query.count() > 0:
                db.query(AdmParameter).filter(AdmParameter.id == id).delete()
                db.commit()
                return True
            else:
                return False
        except Exception as e:
            print(e)
            db.rollback()
            return False
