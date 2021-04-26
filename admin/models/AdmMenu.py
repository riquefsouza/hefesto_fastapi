from sqlalchemy import CHAR, Integer, String, BigInteger, Sequence
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.orm import relationship
from base.database import Base


class AdmMenu(Base):
    __tablename__ = 'adm_menu'

    id = Column('mnu_seq', BigInteger, Sequence('adm_menu_seq'), primary_key=True)
    description = Column('mnu_description', String(255), nullable=False, unique=True)
    idMenuParent = Column('mnu_parent_seq', BigInteger, ForeignKey('adm_menu.mnu_seq'))
    idPage = Column('mnu_pag_seq', BigInteger, ForeignKey('adm_page.pag_seq'))
    order = Column('mnu_order', Integer)
    admMenuParent = relationship('AdmMenu', foreign_keys=idMenuParent)
    admPage = relationship('AdmPage', foreign_keys=idPage)

    def __repr__(self):
        return '<AdmMenu %r>' % self.description
