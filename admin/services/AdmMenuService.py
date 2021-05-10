from fastapi import Depends
from sqlalchemy.orm import Session
from base.database import get_db
from admin.models.AdmMenu import AdmMenu
from admin.schemas.AdmMenuDTO import AdmMenuDTO
from admin.schemas.AdmMenuForm import AdmMenuForm
from base.schemas.MenuItemDTO import MenuItemDTO
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
            dto = self.setTransientSubMenus(item, None, False)
            listaDTO.append(dto)
        return listaDTO

    def setTransientList(self, plist: List[AdmMenu]):
        listaDTO = []
        for item in plist:
            dto = self.setTransient(item)
            listaDTO.append(dto)
        return listaDTO

    def setTransientSubMenus(self, item: AdmMenu, subMenus: List[AdmMenuDTO], bJson: bool):
        dto = AdmMenuDTO(item)
        if item.admPage != None:
            dto.url = item.admPage.url
        else:
            dto.url = None
        dto.subMenus = subMenus

        if bJson:
            return dto.__dict__
        else:
            return dto
    
    def setTransient(self, db: Session, item: AdmMenu):
        listaMenus = self.findByIdMenuParent(db, item.id)
        listaDTO = []
        for menu in listaMenus:
            menuDTO = AdmMenuDTO(menu)
            listaDTO.append(menuDTO.__dict__)

        return self.setTransientSubMenus(item, listaDTO, True)

    def findByIdMenuParent(self, db: Session, idMenuParent: int):
        if idMenuParent != None:
            lista = db.query(AdmMenu).filter_by(idMenuParent = idMenuParent).all()
            #self.setTransientWithoutSubMenus(lista)
            return lista
        
        return []

    def executeSQL(self, db: Session, sql: str):
        rs = db.execute(sql)
        listMenus = []
        for row in rs:
            menuDTO = AdmMenuDTO(None)
            menuDTO.id = row[0]
            menuDTO.description = row[1]
            menuDTO.idMenuParent = row[2]
            menuDTO.idPage = row[3]
            menuDTO.order = row[4]
            menuDTO.admPage = db.query(AdmPage).filter(AdmPage.id == menuDTO.idPage).first()
            menuDTO.url = ""
            menuDTO.subMenus = []            
            listMenus.append(menuDTO)
        return listMenus
    
    def toStrList(self, plist: List[int]):
        strlist = []
        for item in plist:
            strlist.append(str(item))
        values = ",".join(strlist)
        return values 

    def findMenuByIdProfiles(self, db: Session, listIdProfile: List[int], admMenu: AdmMenu):
        sql = f'''select distinct mnu.mnu_seq, mnu.mnu_description, mnu.mnu_parent_seq, mnu.mnu_pag_seq, mnu.mnu_order
            from adm_profile prf 
            inner join adm_page_profile pgl on prf.prf_seq=pgl.pgl_prf_seq 
            inner join adm_page pag on pgl.pgl_pag_seq=pag.pag_seq 
            inner join adm_menu mnu on pag.pag_seq=mnu.mnu_pag_seq 
            where prf.prf_seq in ({self.toStrList(listIdProfile)}) and mnu.mnu_seq > 9 and mnu.mnu_parent_seq={idAdmMenu}
            order by mnu.mnu_seq, mnu.mnu_order'''

        sql = f"select * from find_menu_by_id_profiles('{{{self.toStrList(listIdProfile)}}}',{admMenu.id})"

        return self.executeSQL(db, sql.replace('\n', ''))

    def findAdminMenuByIdProfiles(self, db: Session, listIdProfile: List[int], admMenu: AdmMenu):
        sql = f'''select distinct mnu.mnu_seq, mnu.mnu_description, mnu.mnu_parent_seq, mnu.mnu_pag_seq, mnu.mnu_order
            from adm_profile prf 
            inner join adm_page_profile pgl on prf.prf_seq=pgl.pgl_prf_seq 
            inner join adm_page pag on pgl.pgl_pag_seq=pag.pag_seq 
            inner join adm_menu mnu on pag.pag_seq=mnu.mnu_pag_seq 
            where prf.prf_seq in ({self.toStrList(listIdProfile)}) and mnu.mnu_seq <= 9 and mnu.mnu_parent_seq={idAdmMenu}
            order by mnu.mnu_seq, mnu.mnu_order'''
        
        sql = f"select * from find_Admin_Menu_By_Id_Profiles('{{{self.toStrList(listIdProfile)}}}',{admMenu.id})"            
        
        return self.executeSQL(db, sql.replace('\n', ''))

    def findMenuParentByIdProfiles(self, db: Session, listIdProfile: List[int]):
        sql = f'''select distinct mnu0.mnu_seq, mnu0.mnu_description, mnu0.mnu_parent_seq, mnu0.mnu_pag_seq, mnu0.mnu_order
            from adm_menu mnu0 
            where mnu0.mnu_seq in (
                select mnu0.mnu_parent_seq 
                from adm_profile prf 
                inner join adm_page_profile pgl on prf.prf_seq=pgl.pgl_prf_seq 
                inner join adm_page pag on pgl.pgl_pag_seq=pag.pag_seq 
                inner join adm_menu mnu on pag.pag_seq=mnu0.mnu_pag_seq 
                where prf.prf_seq in ({self.toStrList(listIdProfile)}) and mnu0.mnu_seq > 9
            ) 
            order by mnu0.mnu_order, mnu0.mnu_seq'''

        sql = f"select * from find_menu_parent_by_id_profiles('{{{self.toStrList(listIdProfile)}}}')"

        listMenus = self.executeSQL(db, sql.replace('\n', ''))

        newlist = []
        for admMenu in listMenus:
            plist = self.findMenuByIdProfiles(db, listIdProfile, admMenu)
            plist = self.setTransientWithoutSubMenus(plist)
            admMenu = self.setTransientSubMenus(admMenu, plist, False)
            newlist.append(admMenu)

        return newlist
    
    def findAdminMenuParentByIdProfiles(self, db: Session, listIdProfile: List[int]):
        sql = f'''select distinct mnu0.mnu_seq, mnu0.mnu_description, mnu0.mnu_parent_seq, mnu0.mnu_pag_seq, mnu0.mnu_order
            from adm_menu mnu0 
            where mnu0.mnu_seq in (
                select mnu0.mnu_parent_seq 
                from adm_profile prf 
                inner join adm_page_profile pgl on prf.prf_seq=pgl.pgl_prf_seq 
                inner join adm_page pag on pgl.pgl_pag_seq=pag.pag_seq 
                inner join adm_menu mnu on pag.pag_seq=mnu0.mnu_pag_seq 
                where prf.prf_seq in ({self.toStrList(listIdProfile)}) and mnu0.mnu_seq <= 9
            ) 
            order by mnu0.mnu_order, mnu0.mnu_seq'''

        sql = f"select * from find_admin_menu_parent_by_id_profiles('{{{self.toStrList(listIdProfile)}}}')"

        listMenus = self.executeSQL(db, sql.replace('\n', ''))

        newlist = []
        for admMenu in listMenus:
            plist = self.findAdminMenuByIdProfiles(db, listIdProfile, admMenu)
            plist = self.setTransientWithoutSubMenus(plist)
            admMenu = self.setTransientSubMenus(admMenu, plist, False)
            newlist.append(admMenu)

        return newlist

    def mountMenuItem(self, db: Session, listIdProfile: List[int]):
        lista = []
        
        listMenus = self.findMenuParentByIdProfiles(db, listIdProfile)
        
        for menu in listMenus:
            item = []
            admSubMenus = menu.subMenus

            for submenu in admSubMenus:
                submenuVO = MenuItemDTO(submenu.description, submenu.url, [])
                item.append(submenuVO.__dict__)
            
            vo = MenuItemDTO(menu.description, menu.url, item)
            lista.append(vo.__dict__)
        
        listAdminMenus = self.findAdminMenuParentByIdProfiles(db, listIdProfile)
        
        for menu in listAdminMenus:
            item = []
            admSubMenus = menu.subMenus

            for submenu in admSubMenus:
                submenuVO = MenuItemDTO(submenu.description, submenu.url, [])
                item.append(submenuVO.__dict__)
            
            vo = MenuItemDTO(menu.description, menu.url, item)
            lista.append(vo.__dict__)
    
        return lista
        

