from sqlalchemy import Integer, String, BigInteger
from sqlalchemy.sql.schema import Column
from base.database import Base


class AdmUser(Base):
    __tablename__ = 'adm_user'

    id = Column('usu_seq', BigInteger, primary_key=True)
    active = Column('usu_active', String(1), nullable=False)
    email = Column('usu_email', String(255))
    login = Column('usu_login', String(64), nullable=False)
    name = Column('usu_name', String(64))
    password = Column('usu_password', String(128), nullable=False)
