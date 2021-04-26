import fastapi
from fastapi import Depends, status, Response
from sqlalchemy.orm import Session
from base.database import get_db
from admin.models.AdmParameterCategory import AdmParameterCategory
from admin.schemas.AdmParameterCategoryDTO import AdmParameterCategoryDTO
from admin.schemas.AdmParameterCategoryForm import AdmParameterCategoryForm
from admin.services.AdmParameterCategoryService import AdmParameterCategoryService
from typing import List

router = fastapi.APIRouter()

service = AdmParameterCategoryService()

URL = '/api/v1/admParameterCategory'

@router.get(URL, status_code=status.HTTP_200_OK)
def listAll(db: Session = Depends(get_db)):
    return service.findAll(db)

@router.get(URL + '/{id}', status_code=status.HTTP_200_OK)
def findById(id: int, response: Response, db: Session = Depends(get_db)):
    admParameterCategory = service.findById(db, id)
    if admParameterCategory!=None:
        return admParameterCategory
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return ""

@router.post(URL, status_code=status.HTTP_201_CREATED)
def save(form: AdmParameterCategoryForm, response: Response, db: Session = Depends(get_db)):
    admParameterCategory = service.save(db, form)
    if admParameterCategory!=None:
        dto = AdmParameterCategoryDTO(admParameterCategory)
        return dto.to_json()
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return ""

@router.put(URL + '/{id}', status_code=status.HTTP_200_OK)
def update(id: int, form: AdmParameterCategoryForm, response: Response, db: Session = Depends(get_db)):
    admParameterCategory = service.update(db, id, form)
    if admParameterCategory!=None:
        dto = AdmParameterCategoryDTO(admParameterCategory)
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
