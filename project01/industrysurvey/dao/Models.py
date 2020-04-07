from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

#
# class CustomerData(Base):
#     __tablename__ = 'customerData'
#     customerCd = Column(String, primary_key=True)
#     customerName = Column(String)
#     fld1 = Column(Float)


class AllCustomerMaster(Base):
    __tablename__ = "AllCustomerMaster"
    CustomerCd: str = Column(String, primary_key=True, nullable=False)
    CustomerName: str = Column(String)
    CustomerKanaName: str = Column(String)
    CustomerShortName: str = Column(String)
    ExcludeLaw: bool = Column(Boolean)
    HeadOfficeZipCd: str = Column(String)
    HeadOfficeAddress: str = Column(String)
    HeadOfficeTel: str = Column(String)

    def __init__(self, xldto):
        self.CustomerCd = xldto.xlCustomerCd
        self.CustomerName = xldto.xlCustomerName


class CustomerMaster(Base):
    __tablename__ = 'customerMaster'
    customerCd = Column(String, primary_key=True, nullable=False)
    customerName = Column(String)
    customerKanaName = Column(String)
    customerShortName = Column(String)
    excludeLaw: bool = Column(Boolean)  # False
    headOfficeZipCd: str = Column(String)
    headOfficeAddress: str = Column(String)
    headOfficeTel: str = Column(String)
    headOfficeFax: str = Column(String)
    branchOfficeZipCd: str = Column(String)
    branchOfficeAddress: str = Column(String)
    branchOfficeTel: str = Column(String)
    branchOfficeFax: str = Column(String)
    repName: str = Column(String)
    repKanaName: str = Column(String)
    repJobTitle: str = Column(String)
    repBirthday: str = Column(String)
    employees: int = Column(Integer)
    employeeMonth: str = Column(String)
    employeeYear: str = Column(String)
    capitalForm: int = Column(Integer)
    corporateType: str = Column(String)  # shapes 株式 有限 その他
    otherCorpType: str = Column(String)  # Null
    customerCapital: float = Column(Float)
    establishedMonth: str = Column(String)
    establishedYear: str = Column(String)
    accountClosingMonth: int = Column(Integer)
    returnOnEquity: float = Column(Float)
    ISO9001Certif: str = Column(String)
    ISO9001ResistedNo: str = Column(String)
    ISO9001CertifPlanYM: str = Column(String)
    ISO14001Certif: str = Column(String)
    ISO14001ResistedNo: str = Column(String)
    ISO14001CertifPlanYM: str = Column(String)
    otherCertif: str = Column(String)
    CustomerCategory: str = Column(String)  # Null
    CustomerBizType: str = Column(String)  # shapes
    picName: str = Column(String)
    picKanaName: str = Column(String)
    PicEmailAddress: str = Column(String)
    picDept: str = Column(String)
    picPosition: str = Column(String)
    sameHeadOffice: str = Column(String)
    contactZipCd: str = Column(String)
    contactAddress: str = Column(String)
    contactTel: str = Column(String)
    contactFax: str = Column(String)

    stockstatus = relationship("StockStatusMaster", order_by="StockStatusMaster.customerCd",
                               uselist=False, backref="customerMaster")

    bizcondition = relationship("BizConditionsMaster", order_by="StockStatusMaster.customerCd",
                                uselist=False, backref="customerMaster")

    mainsupplier = relationship("BizConditionsMaster", order_by="StockStatusMaster.customerCd",
                                uselist=False, backref="customerMaster")

    mainproduct = relationship("MainProductMaster", order_by="StockStatusMaster.customerCd",
                               uselist=False, backref="customerMaster")


class StockStatusMaster(Base):
    __tablename__ = "stockStatusMaster"
    CustomerCd: str = Column(String, ForeignKey("customerMaster.customerCd"), primary_key=True)
    stockListingStatus: str = Column(String)
    stockMarket: str = Column(String)
    MainStockholder_1: str = Column(String)
    MainStockholder_2: str = Column(String)
    MainStockholder_3: str = Column(String)
    MainStockholder_4: str = Column(String)
    MainStockholder_5: str = Column(String)
    RatioSH_1: float = Column(Float)
    RatioSH_2: float = Column(Float)
    RatioSH_3: float = Column(Float)
    RatioSH_4: float = Column(Float)
    RatioSH_5: float = Column(Float)


class BizConditionsMaster(Base):
    __tablename__ = "bizConditionsMaster"
    CustomerCd: str = Column(String, ForeignKey("customerMaster.customerCd"), primary_key=True)
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
    curPrdOrdinaryincome: int = Column(Integer)
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
    lastPrdOrdinaryincome: int = Column(Integer)
    curPrdMainProducts: str = Column(String)


class MainSupplierMaster(Base):
    __tablename__ = "mainSupplierMaster"
    CustomerCd: str = Column(String, ForeignKey("customerMaster.customerCd"), primary_key=True)
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


class MainProductMaster(Base):
    __tablename__ = "mainProductMaster"
    CustomerCd: str = Column(String, ForeignKey("customerMaster.customerCd"), primary_key=True)
    MainProducts_1: str = Column(String)
    MainProducts_2: str = Column(String)
    MainProducts_3: str = Column(String)
    MainProducts_4: str = Column(String)
    MainProducts_5: str = Column(String)
