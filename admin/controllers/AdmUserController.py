import fastapi
from fastapi import Depends
from sqlalchemy.orm import Session
from base.database import get_db
from admin.models.AdmUser import AdmUser
from admin.schemas.AdmUserDTO import AdmUserDTO

router = fastapi.APIRouter()

URL = '/api/v1/admUser'

@router.get(URL)
def get_by_id(id: int, db: Session = Depends(get_db)):
    return db.query(AdmUser).filter(AdmUser.id == id).first()


@router.post(URL)
def save(form: AdmUserDTO, db: Session = Depends(get_db)):
    admUser_new = AdmUser(
        active=form.active,
        email=form.email,
        login=form.login,
        name=form.name,
        password=form.password
    )
    db.add(admUser_new)
    db.commit()
    return {
        "admUser_id": admUser_new.id
    }
