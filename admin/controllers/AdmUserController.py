import fastapi
from fastapi import Depends
from sqlalchemy.orm import Session
from base.database import get_db
from admin.models.AdmUser import AdmUser
from admin.schemas.AdmUserDTO import AdmUserDTO
from admin.services.AdmUserService import AdmUserService

router = fastapi.APIRouter()

service = AdmUserService()

URL = '/api/v1/admUser'

@router.get(URL)
def findById(id: int, db: Session = Depends(get_db)):
    return service.findById(db, id)

@router.post(URL)
def save(form: AdmUserDTO, db: Session = Depends(get_db)):
    newAdmUser = service.save(db, form)
    return {
        "admUser_id": newAdmUser.id
    }

@router.delete(URL)
def delete(id: int, db: Session = Depends(get_db)):
    bOk: bool = service.delete(db, id)
    return {"success": bOk}
