import fastapi
from fastapi import Depends, status, Response
from sqlalchemy.orm import Session
from base.database import get_db
from admin.models.AdmParameter import AdmParameter
from admin.schemas.AdmParameterDTO import AdmParameterDTO
from admin.schemas.AdmParameterForm import AdmParameterForm
from admin.services.AdmParameterService import AdmParameterService
from typing import List
from base.services.AuthHandlerService import AuthHandlerService
from base.schemas.UserDTO import UserDTO

router = fastapi.APIRouter()
authHandler = AuthHandlerService()
service = AdmParameterService()

URL = '/api/v1/admParameter'

@router.get(URL, status_code=status.HTTP_200_OK)
def listAll(user: UserDTO = Depends(authHandler.auth_wrapper), 
    db: Session = Depends(get_db)):
    return service.findAll(db)

@router.get(URL + '/{id}', status_code=status.HTTP_200_OK)
def findById(id: int, response: Response, 
    user: UserDTO = Depends(authHandler.auth_wrapper), db: Session = Depends(get_db)):
    admParameter = service.findById(db, id)
    if admParameter!=None:
        return admParameter
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return ""

@router.post(URL, status_code=status.HTTP_201_CREATED)
def save(form: AdmParameterForm, response: Response, 
    user: UserDTO = Depends(authHandler.auth_wrapper), db: Session = Depends(get_db)):
    admParameter = service.save(db, form)
    if admParameter!=None:
        #dto = AdmParameterDTO(admParameter)
        #return dto.to_json()
        return admParameter
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return ""

@router.put(URL + '/{id}', status_code=status.HTTP_200_OK)
def update(id: int, form: AdmParameterForm, response: Response, 
    user: UserDTO = Depends(authHandler.auth_wrapper), db: Session = Depends(get_db)):
    admParameter = service.update(db, id, form)
    if admParameter!=None:
        #dto = AdmParameterDTO(admParameter)
        #return dto.to_json()
        return admParameter
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
