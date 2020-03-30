from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CustomerData(Base):
    __tablename__ = 'customerData'
    customerCd = Column(String, primary_key=True)
    customerName = Column(String)
    fld1 = Column(None)
