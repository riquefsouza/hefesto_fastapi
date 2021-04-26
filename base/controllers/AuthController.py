import fastapi
from fastapi import HTTPException, Depends
from base.services.AuthHandlerService import AuthHandlerService
from base.schemas.AuthDetailsSchema import AuthDetailsSchema

router = fastapi.APIRouter()

service = AuthHandlerService()
users = []

URL = '/api/v1/auth'


@router.post(URL + '/register')
def register(auth_details: AuthDetailsSchema):
	if any(x['username'] == auth_details.username for x in users):
		raise HTTPException(status_code=400, detail='Username is taken')

	hashed_password = service.get_password_hash(auth_details.password)
	users.append({
		'username': auth_details.username,
		'password': auth_details.password
	})	
	return
	
@router.post(URL + '/login')
def login(auth_details: AuthDetailsSchema):
	user = None
	for x in users:
		if x['username'] == auth_details.username:
			user = x
			break

	if (user is None) or (not service.verify_password(auth_details.password, user['password'])):
		raise HTTPException(status_code=401, detail='Invalid username and/or password')

	token = service.encode_token(user['username'])	
	return { 'token': token }

@router.get(URL + '/unprotected')
def unprotected():
	return {'hello':'world'}
	
@router.get(URL + '/protected')
def protected(username=Depends(service.auth_wrapper)):
	return { 'name': username }
