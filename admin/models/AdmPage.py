from sqlalchemy import CHAR, Integer, String, BigInteger, Sequence
from sqlalchemy.sql.schema import Column
from base.database import Base


class AdmPage(Base):
    __tablename__ = 'adm_page'

    id = Column('pag_seq', BigInteger, Sequence('adm_page_seq'), primary_key=True)
    description = Column('pag_description', String(255), nullable=False, unique=True)
    url = Column('pag_url', String(255), nullable=False, unique=True)

    def __repr__(self):
        return '<AdmPage %r>' % self.description
