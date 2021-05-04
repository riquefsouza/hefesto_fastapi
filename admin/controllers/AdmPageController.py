import fastapi
from fastapi import Depends, status, Response
from sqlalchemy.orm import Session
from base.database import get_db
from admin.models.AdmPage import AdmPage
from admin.schemas.AdmPageDTO import AdmPageDTO
from admin.schemas.AdmPageForm import AdmPageForm
from admin.services.AdmPageService import AdmPageService
from typing import List
from base.services.AuthHandlerService import AuthHandlerService
from base.schemas.UserDTO import UserDTO

router = fastapi.APIRouter()
authHandler = AuthHandlerService()
service = AdmPageService()

URL = '/api/v1/admPage'

@router.get(URL, status_code=status.HTTP_200_OK)
def listAll(user: UserDTO = Depends(authHandler.auth_wrapper), 
    db: Session = Depends(get_db)):
    return service.findAll(db)

@router.get(URL + '/{id}', status_code=status.HTTP_200_OK)
def findById(id: int, response: Response, 
    user: UserDTO = Depends(authHandler.auth_wrapper), db: Session = Depends(get_db)):
    admPage = service.findById(db, id)
    if admPage!=None:
        return admPage
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return ""

@router.post(URL, status_code=status.HTTP_201_CREATED)
def save(form: AdmPageForm, response: Response, 
    user: UserDTO = Depends(authHandler.auth_wrapper), db: Session = Depends(get_db)):
    admPage = service.save(db, form)
    if admPage!=None:
        dto = AdmPageDTO(admPage)
        return dto.to_json()
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return ""

@router.put(URL + '/{id}', status_code=status.HTTP_200_OK)
def update(id: int, form: AdmPageForm, response: Response, 
    user: UserDTO = Depends(authHandler.auth_wrapper), db: Session = Depends(get_db)):
    admPage = service.update(db, id, form)
    if admPage!=None:
        dto = AdmPageDTO(admPage)
        return dto.to_json()
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return ""

@router.delete(URL, status_code=status.HTTP_200_OK)
def delete(id: int, response: Response, 
    user: UserDTO = Depends(authHandler.auth_wrapper), db: Session = Depends(get_db)):
    bOk: bool = service.delete(db, id)
    if bOk:
        response.status_code = status.HTTP_200_OK
        return ""
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return ""
