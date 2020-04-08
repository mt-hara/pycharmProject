from dao.BaseEngine import MetaBase
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey

Base = MetaBase

class MainSupplierMaster(Base):
    __tablename__ = "mainduppliermaster"
    customerCd: str = Column(String, ForeignKey("customermaster.customerCd"), primary_key=True)
    mainSupplier_1: str = Column(String)
    mainSupplier_2: str = Column(String)
    mainSupplier_3: str = Column(String)
    mainSupplier_4: str = Column(String)
    mainSupplier_5: str = Column(String)
    mainSupplierValue_1: int = Column(Integer)
    mainSupplierValue_2: int = Column(Integer)
    mainSupplierValue_3: int = Column(Integer)
    mainSupplierValue_4: int = Column(Integer)
    mainSupplierValue_5: int = Column(Integer)
    mainSupplierRatio_1: float = Column(Float)
    mainSupplierRatio_2: float = Column(Float)
    mainSupplierRatio_3: float = Column(Float)
    mainSupplierRatio_4: float = Column(Float)
    mainSupplierRatio_5: float = Column(Float)
