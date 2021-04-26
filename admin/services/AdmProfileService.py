from fastapi import Depends
from sqlalchemy.orm import Session
from base.database import get_db
from admin.models.AdmProfile import AdmProfile
from admin.schemas.AdmProfileDTO import AdmProfileDTO
from admin.schemas.AdmProfileForm import AdmProfileForm

class AdmProfileService:
    def __init__(self):
        pass

    def findAll(self, db: Session):
        return db.query(AdmProfile).all()

    def findById(self, db: Session, id: int):
        return db.query(AdmProfile).filter(AdmProfile.id == id).first()

    def save(self, db: Session, form: AdmProfileForm):
        try:
            admProfile = form.to_AdmProfile()
            db.add(admProfile)
            db.commit()
            return admProfile
        except Exception as e:
            print(e)
            db.rollback()
            return None

    def update(self, db: Session, id: int, form: AdmProfileForm):
        try:
            admProfile: AdmProfile = db.query(AdmProfile).get(id)
            if admProfile != None:
                admProfile = form.from_AdmProfile(admProfile)
                db.commit()
                return admProfile
            else:
                return None
        except Exception as e:
            print(e)
            db.rollback()
            return None

    def delete(self, db: Session, id: int):
        try:
            query = db.query(AdmProfile).filter_by(id=id)
            if query.count() > 0:
                db.query(AdmProfile).filter(AdmProfile.id == id).delete()
                db.commit()
                return True
            else:
                return False
        except Exception as e:
            print(e)
            db.rollback()
            return False
