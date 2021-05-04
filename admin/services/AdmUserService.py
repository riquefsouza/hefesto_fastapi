from fastapi import Depends
from sqlalchemy.orm import Session
from base.database import get_db
from admin.models.AdmUser import AdmUser
from admin.schemas.AdmUserDTO import AdmUserDTO
from admin.schemas.AdmUserForm import AdmUserForm
#import bcrypt
from passlib.context import CryptContext

class AdmUserService:
    bcrypt = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def __init__(self):
        pass

    def findAll(self, db: Session):
        return db.query(AdmUser).all()

    def findById(self, db: Session, id: int):
        return db.query(AdmUser).filter(AdmUser.id == id).first()

    def save(self, db: Session, form: AdmUserForm):
        try:
            admUser = form.to_AdmUser()
            db.add(admUser)
            db.commit()
            return admUser
        except Exception as e:
            print(e)
            db.rollback()
            return None

    def update(self, db: Session, id: int, form: AdmUserForm):
        try:
            admUser: AdmUser = db.query(AdmUser).get(id)
            if admUser != None:
                admUser = form.from_AdmUser(admUser)
                db.commit()
                return admUser
            else:
                return None
        except Exception as e:
            print(e)
            db.rollback()
            return None

    def delete(self, db: Session, id: int):
        try:
            query = db.query(AdmUser).filter_by(id=id)
            if query.count() > 0:
                db.query(AdmUser).filter(AdmUser.id == id).delete()
                db.commit()
                return True
            else:
                return False
        except Exception as e:
            print(e)
            db.rollback()
            return False

    def authenticate(self, db: Session, login: str, password: str):
        admUser = db.query(AdmUser).filter(AdmUser.login == login).first()

        if admUser != None:
            if self.verifyPassword(password, admUser.password):
                return admUser

        return None

    def verifyPassword(self, password: str, hashPassword: str):
        #return bcrypt.checkpw(password, hashPassword)
        return self.bcrypt.verify(password, hashPassword)

    def register(self, model: AdmUser):
        #hash = bcrypt.hashpw(model.password.encode('utf8'), bcrypt.gensalt(10))
        hash = self.bcrypt.hash(model.password.encode('utf8'))
        model.password = hash
