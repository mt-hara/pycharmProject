from sqlalchemy import Column, Integer, String, Float, Boolean, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class AllCustomerMaster(Base):
    __tablename__ = 'AllCustomerMaster'
    CustomerCd = Column(String, primary_key=True, nullable=False)
    CustomerName = Column(String)
    CustomerKanaName = Column(String)
    CustomerShortName = Column(String)
    StockStatusMaster = relationship("StockStatusMaster")

    # def __init__(self,cd, name):
    #     self.CustomerCd = cd
    #     self.CustomerName = name

class StockStatusMaster(Base):
    __tablename__ = "StockStatusMaster"
    CustomerCd = Column(String,ForeignKey('AllCustomerMaster.CustomerCd'), primary_key=True)
    stockListingStatus = Column(String)
    MainStockholder_1 = Column(String)
    MainStockholder_2 = Column(String)
    MainStockholder_3 = Column(String)
    MainStockholder_4 = Column(String)
    MainStockholder_5 = Column(String)

    # def __init__(self,cd,name):
    #     self.stockListingStatus = cd
    #     self.MainStockholder_1 = name

