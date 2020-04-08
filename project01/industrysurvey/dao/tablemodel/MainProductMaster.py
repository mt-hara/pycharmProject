from dao.BaseEngine import MetaBase
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey

Base = MetaBase

class MainProductMaster(Base):
    __tablename__ = "mainproductmaster"
    customerCd: str = Column(String, ForeignKey("customermaster.customerCd"), primary_key=True)
    mainProducts_1: str = Column(String)
    mainProducts_2: str = Column(String)
    mainProducts_3: str = Column(String)
    mainProducts_4: str = Column(String)
    mainProducts_5: str = Column(String)