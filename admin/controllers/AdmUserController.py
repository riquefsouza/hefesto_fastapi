import fastapi
from fastapi import Depends, status, Response
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

@router.get(URL, status_code=status.HTTP_200_OK)
def listAll(db: Session = Depends(get_db)):
    return service.findAll(db)

@router.get(URL + '/{id}', status_code=status.HTTP_200_OK)
def findById(id: int, response: Response, db: Session = Depends(get_db)):
    admUser = service.findById(db, id)
    if admUser!=None:
        return admUser
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return ""

@router.post(URL, status_code=status.HTTP_201_CREATED)
def save(form: AdmUserForm, response: Response, db: Session = Depends(get_db)):
    admUser = service.save(db, form)
    if admUser!=None:
        dto = AdmUserDTO(admUser)
        return dto.to_json()
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return ""

@router.put(URL + '/{id}', status_code=status.HTTP_200_OK)
def update(id: int, form: AdmUserForm, response: Response, db: Session = Depends(get_db)):
    admUser = service.update(db, id, form)
    if admUser!=None:
        dto = AdmUserDTO(admUser)
        return dto.to_json()
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return ""

@router.delete(URL, status_code=status.HTTP_200_OK)
def delete(id: int, response: Response, db: Session = Depends(get_db)):
    bOk: bool = service.delete(db, id)
    if bOk:
        response.status_code = status.HTTP_200_OK
        return ""
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return ""
