from dao.BaseEngine import MetaBase
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey


class BizConditionsMaster(MetaBase):
    __tablename__ = "bizconditionsmaster"
    # customerCd: str = Column(String)
    customerCd: str = Column(String, ForeignKey("customermaster.customerCd"), primary_key=True)
    mainCustomer_1: str = Column(String)
    mainCustomer_2: str = Column(String)
    mainCustomer_3: str = Column(String)
    mainCustomer_4: str = Column(String)
    mainCustomer_5: str = Column(String)
    curPrdYear: str = Column(String)
    curPrdSales_1: int = Column(Integer)
    curPrdSales_2: int = Column(Integer)
    curPrdSales_3: int = Column(Integer)
    curPrdSales_4: int = Column(Integer)
    curPrdSales_5: int = Column(Integer)
    curPrdSales_Our: int = Column(Integer)
    curPrdSales_Other: int = Column(Integer)
    curPrdSalesRatio_1: float = Column(Float)
    curPrdSalesRatio_2: float = Column(Float)
    curPrdSalesRatio_3: float = Column(Float)
    curPrdSalesRatio_4: float = Column(Float)
    curPrdSalesRatio_5: float = Column(Float)
    curPrdSalesRatio_Our: float = Column(Float)
    curPrdSalesRatio_Othor: float = Column(Float)
    curPrdSales_Sum: int = Column(Integer)
    curPrdOperatingProfit: int = Column(Integer)
    curPrdOrdinaryIncome: int = Column(Integer)
    prevPrdYear: str = Column(String)
    prevPrdSales_1: int = Column(Integer)
    prevPrdSales_2: int = Column(Integer)
    prevPrdSales_3: int = Column(Integer)
    prevPrdSales_4: int = Column(Integer)
    prevPrdSales_5: int = Column(Integer)
    prevPrdSales_Our: int = Column(Integer)
    prevPrdSales_Other: int = Column(Integer)
    prevPrdSalesRatio_1: float = Column(Float)
    prevPrdSalesRatio_2: float = Column(Float)
    prevPrdSalesRatio_3: float = Column(Float)
    prevPrdSalesRatio_4: float = Column(Float)
    prevPrdSalesRatio_5: float = Column(Float)
    prevPrdSalesRatio_Our: float = Column(Float)
    prevPrdSalesRatio_Other: float = Column(Float)
    prevPrdSales_Sum: int = Column(Integer)
    prevPrdOperatingProfit: int = Column(Integer)
    prevPrdOrdinaryIncome: int = Column(Integer)
    lastPrdYear: str = Column(String)
    lastPrdSales_1: int = Column(Integer)
    lastPrdSales_2: int = Column(Integer)
    lastPrdSales_3: int = Column(Integer)
    lastPrdSales_4: int = Column(Integer)
    lastPrdSales_5: int = Column(Integer)
    lastPrdSales_Our: int = Column(Integer)
    lastPrdSales_Other: int = Column(Integer)
    lastPrdSalesRatio_1: float = Column(Float)
    lastPrdSalesRatio_2: float = Column(Float)
    lastPrdSalesRatio_3: float = Column(Float)
    lastPrdSalesRatio_4: float = Column(Float)
    lastPrdSalesRatio_5: float = Column(Float)
    lastPrdSalesRatio_Our: float = Column(Float)
    lastPrdSalesRatio_Other: float = Column(Float)
    lastPrdSales_sum: int = Column(Integer)
    lastPrdOperatingProfit: int = Column(Integer)
    lastPrdOrdinaryIncome: int = Column(Integer)
    curPrdMainProducts: str = Column(String)

    def set_data(self, xldto):
        self.mainCustomer_1: str = xldto.xlmainCustomer_1
        self.mainCustomer_2: str = xldto.xlmainCustomer_2
        self.mainCustomer_3: str = xldto.xlmainCustomer_3
        self.mainCustomer_4: str = xldto.xlmainCustomer_4
        self.mainCustomer_5: str = xldto.xlmainCustomer_5
        self.curPrdYear: str = xldto.xlCurPrdYear
        self.curPrdSales_1: int = xldto.xlCurPrdSales_1
        self.curPrdSales_2: int = xldto.xlCurPrdSales_2
        self.curPrdSales_3: int = xldto.xlCurPrdSales_3
        self.curPrdSales_4: int = xldto.xlCurPrdSales_4
        self.curPrdSales_5: int = xldto.xlCurPrdSales_5
        self.curPrdSales_Our: int = xldto.xlCurPrdSales_Our
        self.curPrdSales_Other: int = xldto.xlCurPrdSales_Other
        self.curPrdSalesRatio_1: float = xldto.xlCurPrdSalesRatio_1
        self.curPrdSalesRatio_2: float = xldto.xlCurPrdSalesRatio_2
        self.curPrdSalesRatio_3: float = xldto.xlCurPrdSalesRatio_3
        self.curPrdSalesRatio_4: float = xldto.xlCurPrdSalesRatio_4
        self.curPrdSalesRatio_5: float = xldto.xlCurPrdSalesRatio_5
        self.curPrdSalesRatio_Our: float = xldto.xlCurPrdSalesRatio_Our
        self.curPrdSalesRatio_Othor: float = xldto.xlCurPrdSalesRatio_Othor
        self.curPrdSales_Sum: int = xldto.xlCurPrdSales_Sum
        self.curPrdOperatingProfit: int = xldto.xlCurPrdOperatingProfit
        self.curPrdOrdinaryIncome: int = xldto.xlCurPrdOrdinaryIncome
        self.prevPrdYear: str = xldto.xlPrevPrdYear
        self.prevPrdSales_1: int = xldto.xlPrevPrdSales_1
        self.prevPrdSales_2: int = xldto.xlPrevPrdSales_2
        self.prevPrdSales_3: int = xldto.xlPrevPrdSales_3
        self.prevPrdSales_4: int = xldto.xlPrevPrdSales_4
        self.prevPrdSales_5: int = xldto.xlPrevPrdSales_5
        self.prevPrdSales_Our: int = xldto.xlPrevPrdSales_Our
        self.prevPrdSales_Other: int = xldto.xlPrevPrdSales_Other
        self.prevPrdSalesRatio_1: float = xldto.xlPrevPrdSalesRatio_1
        self.prevPrdSalesRatio_2: float = xldto.xlPrevPrdSalesRatio_2
        self.prevPrdSalesRatio_3: float = xldto.xlPrevPrdSalesRatio_3
        self.prevPrdSalesRatio_4: float = xldto.xlPrevPrdSalesRatio_4
        self.prevPrdSalesRatio_5: float = xldto.xlPrevPrdSalesRatio_5
        self.prevPrdSalesRatio_Our: float = xldto.xlPrevPrdSalesRatio_Our
        self.prevPrdSalesRatio_Other: float = xldto.xlPrevPrdSalesRatio_Other
        self.prevPrdSales_Sum: int = xldto.xlPrevPrdSales_Sum
        self.prevPrdOperatingProfit: int = xldto.xlPrevPrdOperatingProfit
        self.prevPrdOrdinaryIncome: int = xldto.xlPrevPrdOrdinaryIncome
        self.lastPrdYear: str = xldto.xlLastPrdYear
        self.lastPrdSales_1: int = xldto.xlLastPrdSales_1
        self.lastPrdSales_2: int = xldto.xlLastPrdSales_2
        self.lastPrdSales_3: int = xldto.xlLastPrdSales_3
        self.lastPrdSales_4: int = xldto.xlLastPrdSales_4
        self.lastPrdSales_5: int = xldto.xlLastPrdSales_5
        self.lastPrdSales_Our: int = xldto.xlLastPrdSales_Our
        self.lastPrdSales_Other: int = xldto.xlLastPrdSales_Other
        self.lastPrdSalesRatio_1: float = xldto.xlLastPrdSalesRatio_1
        self.lastPrdSalesRatio_2: float = xldto.xlLastPrdSalesRatio_2
        self.lastPrdSalesRatio_3: float = xldto.xlLastPrdSalesRatio_3
        self.lastPrdSalesRatio_4: float = xldto.xlLastPrdSalesRatio_4
        self.lastPrdSalesRatio_5: float = xldto.xlLastPrdSalesRatio_5
        self.lastPrdSalesRatio_Our: float = xldto.xlLastPrdSalesRatio_Our
        self.lastPrdSalesRatio_Other: float = xldto.xlLastPrdSalesRatio_Other
        self.lastPrdSales_sum: int = xldto.xlLastPrdSales_Sum
        self.lastPrdOperatingProfit: int = xldto.xlLastPrdOperatingProfit
        self.lastPrdOrdinaryIncome: int = xldto.xlLastPrdOrdinaryIncome
        self.curPrdMainProducts: str = xldto.xlCurPrdMainProducts
