from fastapi import Depends
from sqlalchemy.orm import Session
from base.database import get_db
from admin.models.AdmParameterCategory import AdmParameterCategory
from admin.schemas.AdmParameterCategoryDTO import AdmParameterCategoryDTO
from admin.schemas.AdmParameterCategoryForm import AdmParameterCategoryForm

class AdmParameterCategoryService:
    def __init__(self):
        pass

    def findAll(self, db: Session):
        return db.query(AdmParameterCategory).all()

    def findById(self, db: Session, id: int):
        return db.query(AdmParameterCategory).filter(AdmParameterCategory.id == id).first()

    def save(self, db: Session, form: AdmParameterCategoryForm):
        try:
            admParameterCategory = form.to_AdmParameterCategory()
            db.add(admParameterCategory)
            db.commit()
            return admParameterCategory
        except Exception as e:
            print(e)
            db.rollback()
            return None

    def update(self, db: Session, id: int, form: AdmParameterCategoryForm):
        try:
            admParameterCategory: AdmParameterCategory = db.query(AdmParameterCategory).get(id)
            if admParameterCategory != None:
                admParameterCategory = form.from_AdmParameterCategory(admParameterCategory)
                db.commit()
                return admParameterCategory
            else:
                return None
        except Exception as e:
            print(e)
            db.rollback()
            return None

    def delete(self, db: Session, id: int):
        try:
            query = db.query(AdmParameterCategory).filter_by(id=id)
            if query.count() > 0:
                db.query(AdmParameterCategory).filter(AdmParameterCategory.id == id).delete()
                db.commit()
                return True
            else:
                return False
        except Exception as e:
            print(e)
            db.rollback()
            return False
