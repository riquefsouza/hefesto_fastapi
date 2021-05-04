import fastapi
from fastapi import Depends, status, Response
from sqlalchemy.orm import Session
from base.database import get_db
from admin.services.AdmUserService import AdmUserService
from base.schemas.UserDTO import UserDTO
from base.schemas.TokenDTO import TokenDTO
from base.schemas.LoginForm import LoginForm
from base.services.AuthHandlerService import AuthHandlerService
import jwt
from datetime import datetime, timedelta

router = fastapi.APIRouter()

service = AdmUserService()
authHandler = AuthHandlerService()

URL = '/auth'

@router.post(URL, status_code=status.HTTP_200_OK)
def login(loginForm: LoginForm, response: Response, db: Session = Depends(get_db)):
    try:
        if (loginForm != None and loginForm.login != None and loginForm.password != None):
            admUser = service.authenticate(db, loginForm.login, loginForm.password)
            if admUser!=None:
                user = UserDTO()
                user.id = admUser.id
                user.name = admUser.name
                user.email = admUser.email

                dto = authHandler.encode_token(user)                
        
                response.status_code = status.HTTP_200_OK
                return dto.to_json()
            else:
                print(f'Authentication failed for user {loginForm.login}')
                print('No token generated')
                response.status_code = status.HTTP_401_UNAUTHORIZED
                return "{ 'message': 'Authentication failed for user " + loginForm.login + "' }"
        else:    
            response.status_code = status.HTTP_400_BAD_REQUEST
            return ""
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return ""
