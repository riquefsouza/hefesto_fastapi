from sqlalchemy import CHAR, Integer, String, BigInteger, Sequence
from sqlalchemy.sql.schema import Column
from base.database import Base


class AdmUser(Base):
    __tablename__ = 'adm_user'

    id = Column('usu_seq', BigInteger, Sequence('adm_user_seq'), primary_key=True)
    active = Column('usu_active', CHAR, nullable=False, default='N')
    email = Column('usu_email', String(255))
    login = Column('usu_login', String(64), nullable=False)
    name = Column('usu_name', String(64))
    password = Column('usu_password', String(128), nullable=False)
