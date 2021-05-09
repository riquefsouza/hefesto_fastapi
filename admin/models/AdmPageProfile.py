from sqlalchemy import CHAR, Integer, String, BigInteger, Sequence
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.orm import relationship
from base.database import Base


class AdmPageProfile(Base):
    __tablename__ = 'adm_page_profile'

    id = Column('pgl_seq', BigInteger, Sequence('adm_page_profile_seq'), primary_key=True)
    idProfile = Column('pgl_prf_seq', BigInteger, ForeignKey('adm_profile.prf_seq'), nullable=False)
    idPage = Column('pgl_pag_seq', BigInteger, ForeignKey('adm_page.pag_seq'), nullable=False)
    admProfile = relationship('AdmProfile', foreign_keys=idProfile)
    admPage = relationship('AdmPage', foreign_keys=idPage)

    #def __repr__(self):
    #    return '<AdmPageProfile %r>' % self.description
