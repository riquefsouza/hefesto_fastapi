from sqlalchemy import CHAR, Integer, String, BigInteger, Sequence
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.orm import relationship
from base.database import Base


class AdmParameter(Base):
    __tablename__ = 'adm_parameter'

    id = Column('par_seq', BigInteger, Sequence('adm_parameter_seq'), primary_key=True)
    code = Column('par_code', String(64), nullable=False)
    description = Column('par_description', String(255), nullable=False, unique=True)
    idParameterCategory = Column('par_pmc_seq', BigInteger, ForeignKey('adm_parameter_category.pmc_seq'), nullable=False)
    value = Column('par_value', String(4000))
    admParameterCategory = relationship('AdmParameterCategory', foreign_keys=idParameterCategory)

    def __repr__(self):
        return '<AdmParameter %r>' % self.description
