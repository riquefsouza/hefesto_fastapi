import fastapi
from fastapi import Depends
from sqlalchemy.orm import Session
from base.database import get_db
from admin.models.AdmUser import AdmUser
from admin.schemas.AdmUserDTO import AdmUserDTO
from admin.schemas.AdmUserForm import AdmUserForm
from admin.services.AdmUserService import AdmUserService
from typing import List

router = fastapi.APIRouter()

service = AdmUserService()

URL = '/api/v1/admUser'

@router.get(URL)
def findAll(db: Session = Depends(get_db)):
    return service.findAll(db)

@router.get(URL + '/{id}')
def findById(id: int, db: Session = Depends(get_db)):
    return service.findById(db, id)

@router.post(URL)
def save(form: AdmUserForm, db: Session = Depends(get_db)):
    newAdmUser = service.save(db, form)
    return {
        "admUser_id": newAdmUser.id
    }

@router.put(URL + '/{id}')
def save(id: int, form: AdmUserForm, db: Session = Depends(get_db)):
    admUser = service.update(db, id, form)
    dto = AdmUserDTO(admUser)
    return dto.to_json()

@router.delete(URL)
def delete(id: int, db: Session = Depends(get_db)):
    bOk: bool = service.delete(db, id)
    return {"success": bOk}
