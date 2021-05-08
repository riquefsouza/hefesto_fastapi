import fastapi
from fastapi import Depends, status, Response
from sqlalchemy.orm import Session
from base.database import get_db
from admin.models.AdmProfile import AdmProfile
from admin.schemas.AdmProfileDTO import AdmProfileDTO
from admin.schemas.AdmProfileForm import AdmProfileForm
from admin.services.AdmProfileService import AdmProfileService
from typing import List
from base.services.AuthHandlerService import AuthHandlerService
from base.schemas.UserDTO import UserDTO

router = fastapi.APIRouter()
authHandler = AuthHandlerService()
service = AdmProfileService()

URL = '/api/v1/admProfile'

@router.get(URL, status_code=status.HTTP_200_OK)
def listAll(user: UserDTO = Depends(authHandler.auth_wrapper), 
    db: Session = Depends(get_db)):
    return service.findAll(db)

@router.get(URL + '/{id}', status_code=status.HTTP_200_OK)
def findById(id: int, response: Response, 
    user: UserDTO = Depends(authHandler.auth_wrapper), db: Session = Depends(get_db)):
    admProfile = service.findById(db, id)
    if admProfile!=None:
        return admProfile
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return ""

@router.post(URL, status_code=status.HTTP_201_CREATED)
def save(form: AdmProfileForm, response: Response, 
    user: UserDTO = Depends(authHandler.auth_wrapper), db: Session = Depends(get_db)):
    admProfile = service.save(db, form)
    if admProfile!=None:
        dto = AdmProfileDTO(admProfile)
        return dto.to_json()
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return ""

@router.put(URL + '/{id}', status_code=status.HTTP_200_OK)
def update(id: int, form: AdmProfileForm, response: Response, 
    user: UserDTO = Depends(authHandler.auth_wrapper), db: Session = Depends(get_db)):
    admProfile = service.update(db, id, form)
    if admProfile!=None:
        dto = AdmProfileDTO(admProfile)
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

@router.get(URL + '/{pageId}', status_code=status.HTTP_200_OK)
def findProfilesByPage(pageId: int, response: Response, 
    user: UserDTO = Depends(authHandler.auth_wrapper), db: Session = Depends(get_db)):
    listAdmProfile = service.findProfilesByPage(db, pageId)
    if listAdmProfile!=None:
        return listAdmProfile
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return ""

@router.get(URL + '/{userId}', status_code=status.HTTP_200_OK)
def findProfilesByUser(userId: int, response: Response, 
    user: UserDTO = Depends(authHandler.auth_wrapper), db: Session = Depends(get_db)):
    listAdmProfile = service.findProfilesByUser(db, userId)
    if listAdmProfile!=None:
        return listAdmProfile
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return ""



