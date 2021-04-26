from sqlalchemy import CHAR, Integer, String, BigInteger, Sequence
from sqlalchemy.sql.schema import Column
from sqlalchemy.orm import relationship
from base.database import Base


class AdmUserProfile(Base):
    __tablename__ = 'adm_user_profile'

    id = Column('usp_seq', BigInteger, Sequence('adm_user_profile_seq'), primary_key=True)
    idProfile = Column('usp_prf_seq', BigInteger, nullable=False, db.ForeignKey('adm_profile.prf_seq'))
    idUser = Column('usp_use_seq', BigInteger, nullable=False, db.ForeignKey('adm_user.usu_seq'))
    admProfile = relationship('AdmProfile', foreign_keys=idProfile)
    admUser = relationship('AdmUser', foreign_keys=idUser)

    #def __repr__(self):
    #    return '<AdmUserProfile %r>' % self.description
