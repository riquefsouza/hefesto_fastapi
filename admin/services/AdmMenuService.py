from fastapi import Depends
from sqlalchemy.orm import Session
from base.database import get_db
from admin.models.AdmMenu import AdmMenu
from admin.schemas.AdmMenuDTO import AdmMenuDTO
from admin.schemas.AdmMenuForm import AdmMenuForm
from typing import List

class AdmMenuService:
    def __init__(self):
        pass

    def findAll(self, db: Session):
        return db.query(AdmMenu).all()

    def findById(self, db: Session, id: int):
        return db.query(AdmMenu).filter(AdmMenu.id == id).first()

    def save(self, db: Session, form: AdmMenuForm):
        try:
            admMenu = form.to_AdmMenu()
            db.add(admMenu)
            db.commit()
            return admMenu
        except Exception as e:
            print(e)
            db.rollback()
            return None

    def update(self, db: Session, id: int, form: AdmMenuForm):
        try:
            admMenu: AdmMenu = db.query(AdmMenu).get(id)
            if admMenu != None:
                admMenu = form.from_AdmMenu(admMenu)
                db.commit()
                return admMenu
            else:
                return None
        except Exception as e:
            print(e)
            db.rollback()
            return None

    def delete(self, db: Session, id: int):
        try:
            query = db.query(AdmMenu).filter_by(id=id)
            if query.count() > 0:
                db.query(AdmMenu).filter(AdmMenu.id == id).delete()
                db.commit()
                return True
            else:
                return False
        except Exception as e:
            print(e)
            db.rollback()
            return False
    
    def setTransientWithoutSubMenus(self, plist: List[AdmMenu]):
        listaDTO = []
        for item in plist:
            dto = self.setTransientSubMenus(item, None)
            listaDTO.append(dto)
        return listaDTO

    def setTransientList(self, plist: List[AdmMenu]):
        listaDTO = []
        for item in plist:
            dto = self.setTransient(item)
            listaDTO.append(dto)
        return listaDTO

    def setTransientSubMenus(self, item: AdmMenu, subMenus: List[AdmMenuDTO]):
        dto = AdmMenuDTO(item)
        if item.admPage != None:
            dto.url = item.admPage.url
        else:
            dto.url = None
        dto.subMenus = subMenus

        return dto.__dict__
    
    def setTransient(self, db: Session, item: AdmMenu):
        listaMenus = self.findByIdMenuParent(db, item.id)
        listaDTO = []
        for menu in listaMenus:
            menuDTO = AdmMenuDTO(menu)
            listaDTO.append(menuDTO.__dict__)

        return self.setTransientSubMenus(item, listaDTO)

    def findByIdMenuParent(self, db: Session, idMenuParent: int):
        if idMenuParent != None:
            lista = db.query(AdmMenu).filter_by(idMenuParent = idMenuParent).all()
            #self.setTransientWithoutSubMenus(lista)
            return lista
        
        return []

    def findMenuByIdProfiles(self, db: Session, listaIdProfile: List[int], admMenu: AdmMenu):
        pass

    def findAdminMenuByIdProfiles(self, db: Session, listaIdProfile: List[int], admMenu: AdmMenu):
        pass

    def findMenuParentByIdProfiles(self, db: Session, listaIdProfile: List[int]):
        pass
    
    def findAdminMenuParentByIdProfiles(self, db: Session, listaIdProfile: List[int]):
        pass

    def mountMenuItem(self, db: Session, listIdProfile: List[int]):
        pass

