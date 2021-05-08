from fastapi import Depends
from sqlalchemy.orm import Session
from base.database import get_db
from typing import List
from admin.models.AdmPage import AdmPage
from admin.models.AdmProfile import AdmProfile
from admin.models.AdmPageProfile import AdmPageProfile


class AdmPageProfileService:
    def __init__(self):
        pass

    def setTransient(self, db: Session, list: List[AdmPageProfile]):
        for item in list:
            setTransient(db, item)

    def setTransient(self, db: Session, item: AdmPageProfile):
        item.AdmPage = db.query(AdmPage).filter(AdmPage.id == item.idPage).first()
        item.AdmProfile = db.query(AdmProfile).filter(AdmProfile.id == item.idProfile).first()