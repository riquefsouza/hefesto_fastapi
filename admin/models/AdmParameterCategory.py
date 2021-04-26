from sqlalchemy import CHAR, Integer, String, BigInteger, Sequence
from sqlalchemy.sql.schema import Column
from base.database import Base


class AdmParameterCategory(Base):
    __tablename__ = 'adm_parameter_category'

    id = Column('pmc_seq', BigInteger, Sequence('adm_parameter_category_seq'), primary_key=True)
    description = Column('pmc_description', String(64), nullable=False, unique=True)
    order = Column('pmc_order', BigInteger)

    def __repr__(self):
        return '<AdmParameterCategory %r>' % self.description
