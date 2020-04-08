from dao.BaseEngine import MetaBase
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship

# Base = MetaBase


class StockStatusMaster(MetaBase):
    __tablename__ = "stockstatusmaster"
    customerCd: str = Column(String, ForeignKey("customermaster.customerCd"), primary_key=True)
    stockListingStatus: str = Column(String, nullable=True)
    stockMarket: str = Column(String, nullable=True)
    mainStockholder_1: str = Column(String, nullable=True)
    mainStockholder_2: str = Column(String, nullable=True)
    mainStockholder_3: str = Column(String, nullable=True)
    mainStockholder_4: str = Column(String, nullable=True)
    mainStockholder_5: str = Column(String, nullable=True)
    ratioSH_1: float = Column(Float)
    ratioSH_2: float = Column(Float)
    ratioSH_3: float = Column(Float)
    ratioSH_4: float = Column(Float)
    ratioSH_5: float = Column(Float)

    # customer = relationship("CustomerMaster", uselist=False, back_populates="stockstatus")

    def set_data(self, xldto):
        self.stockListingStatus = xldto.xlStockListingStatus
        self.stockMarket = xldto.xlStockMarket
        self.mainStockholder_1 = xldto.xlMainStockholder_1
        self.mainStockholder_2 = xldto.xlMainStockholder_2
        self.mainStockholder_3 = xldto.xlMainStockholder_3
        self.mainStockholder_4 = xldto.xlMainStockholder_4
        self.mainStockholder_5 = xldto.xlMainStockholder_5
        self.ratioSH_1 = xldto.xlRatioSH_1
        self.ratioSH_2 = xldto.xlRatioSH_2
        self.ratioSH_3 = xldto.xlRatioSH_3
        self.ratioSH_4 = xldto.xlRatioSH_4
        self.ratioSH_5 = xldto.xlRatioSH_5