import fastapi
from fastapi import Depends, status, Response
from sqlalchemy.orm import Session
from base.database import get_db
from admin.models.AdmMenu import AdmMenu
from admin.schemas.AdmMenuDTO import AdmMenuDTO
from admin.schemas.AdmMenuForm import AdmMenuForm
from admin.services.AdmMenuService import AdmMenuService
from typing import List

router = fastapi.APIRouter()

service = AdmMenuService()

URL = '/api/v1/admMenu'

@router.get(URL, status_code=status.HTTP_200_OK)
def listAll(db: Session = Depends(get_db)):
    return service.findAll(db)

@router.get(URL + '/{id}', status_code=status.HTTP_200_OK)
def findById(id: int, response: Response, db: Session = Depends(get_db)):
    admMenu = service.findById(db, id)
    if admMenu!=None:
        return admMenu
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return ""

@router.post(URL, status_code=status.HTTP_201_CREATED)
def save(form: AdmMenuForm, response: Response, db: Session = Depends(get_db)):
    admMenu = service.save(db, form)
    if admMenu!=None:
        dto = AdmMenuDTO(admMenu)
        return dto.to_json()
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return ""

@router.put(URL + '/{id}', status_code=status.HTTP_200_OK)
def update(id: int, form: AdmMenuForm, response: Response, db: Session = Depends(get_db)):
    admMenu = service.update(db, id, form)
    if admMenu!=None:
        dto = AdmMenuDTO(admMenu)
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
