from sqlalchemy import CHAR, Integer, String, BigInteger, Sequence
from sqlalchemy.sql.schema import Column
from base.database import Base


class AdmProfile(Base):
    __tablename__ = 'adm_profile'

    id = Column('prf_seq', BigInteger, Sequence('adm_profile_seq'), primary_key=True)
    administrator = Column('prf_administrator', CHAR(1), nullable=False, default='N')
    description = Column('prf_description', String(255), nullable=False, unique=True)
    general = Column('prf_general', CHAR(1), nullable=False, default='N')

    def __repr__(self):
        return '<AdmProfile %r>' % self.name
