from fastapi import Depends
from sqlalchemy.orm import Session
from base.database import get_db
from admin.models.AdmParameter import AdmParameter
from admin.schemas.AdmParameterDTO import AdmParameterDTO
from admin.schemas.AdmParameterCategoryDTO import AdmParameterCategoryDTO
from admin.services.AdmParameterCategoryService import AdmParameterCategoryService
from admin.schemas.AdmParameterForm import AdmParameterForm
from typing import List
import json


class AdmParameterService:
    parameterCategoryService = AdmParameterCategoryService()

    def __init__(self):
        pass

    def findAll(self, db: Session):
        plist = db.query(AdmParameter).all()
        return self.setTransientList(db, plist)

    def findById(self, db: Session, id: int):
        obj = db.query(AdmParameter).filter(AdmParameter.id == id).first()
        return self.setTransient(db, obj)

    def save(self, db: Session, form: AdmParameterForm):
        try:
            admParameter = form.to_AdmParameter()
            db.add(admParameter)
            db.commit()
            return self.setTransient(db, admParameter)
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
                return self.setTransient(db, admParameter)
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

    def setTransientList(self, db: Session, plist: List[AdmParameter]):
        listaDTO = []
        for item in plist:
            dto = self.setTransient(db, item)
            listaDTO.append(dto)
        return listaDTO

    def setTransient(self, db: Session, item: AdmParameter):
        dto = AdmParameterDTO(item)
        parameterCategory = self.parameterCategoryService.findById(db, item.idParameterCategory)
        dto.admParameterCategory = AdmParameterCategoryDTO(parameterCategory).__dict__

        return dto.__dict__
