from sqlalchemy import CHAR, Integer, String, BigInteger, Sequence
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.orm import relationship
from base.database import Base


class AdmUserProfile(Base):
    __tablename__ = 'adm_user_profile'

    id = Column('usp_seq', BigInteger, Sequence('adm_user_profile_seq'), primary_key=True)
    idProfile = Column('usp_prf_seq', BigInteger, ForeignKey('adm_profile.prf_seq'), nullable=False)
    idUser = Column('usp_use_seq', BigInteger, ForeignKey('adm_user.usu_seq'), nullable=False)
    admProfile = relationship('AdmProfile', foreign_keys=idProfile)
    admUser = relationship('AdmUser', foreign_keys=idUser)

    #def __repr__(self):
    #    return '<AdmUserProfile %r>' % self.description
