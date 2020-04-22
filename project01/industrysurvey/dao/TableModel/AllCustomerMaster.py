from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from dao.DAOFunction import YearMonthDayGenerator, YearMonthGenerator, ISOCertifGenerator
Base = declarative_base()


class AllCustomerMaster(Base):
    __tablename__ = "allcustomermaster"
    customerCd: str = Column( String, primary_key=True, nullable=False)
    customerName: str = Column(String, nullable=True)
    customerKanaName: str = Column(String, nullable=True)
    customerShortName: str = Column(String, nullable=True)  # Null
    excludeLaw: bool = Column(Boolean)  # False
    headOfficeZipCd: str = Column(String, nullable=True)
    headOfficeAddress: str = Column(String, nullable=True)
    headOfficeTel: str = Column(String, nullable=True)
    headOfficeFax: str = Column(String, nullable=True)
    branchOfficeZipCd: str = Column(String, nullable=True)
    branchOfficeAddress: str = Column(String, nullable=True)
    branchOfficeTel: str = Column(String, nullable=True)
    branchOfficeFax: str = Column(String, nullable=True)
    repName:str = Column(String, nullable=True)
    repKanaName: str = Column(String, nullable=True)
    repJobTitle: str = Column(String, nullable=True)
    repBirthday: str = Column(String, nullable=True)
    employees: int = Column(Integer, nullable=True)
    employeeYear: str = Column(String, nullable=True)
    employeeMonth: str = Column(String, nullable=True)
    capitalForm: int = Column(Integer, nullable=True)
    corporateType: str = Column(String, nullable=True)  # shapes 株式 有限 その他
    otherCorpType: str =Column(String, nullable=True)  # Null
    customerCapital: float = Column(Float)
    establishedYear:str = Column(String, nullable=True)
    establishedMonth: str = Column(String, nullable=True)
    accountClosingMonth: int = Column(Integer)
    returnOnEquity:float = Column(Float)
    ISO9001Certif: str = Column(String, nullable=True)
    ISO9001ResistedNo: str = Column(String, nullable=True)
    ISO9001CertifPlanYM: str = Column(String, nullable=True)
    ISO14001Certif: str = Column(String, nullable=True)
    ISO14001ResistedNo: str = Column(String, nullable=True)
    ISO14001CertifPlanYM: str = Column(String, nullable=True)
    otherCertif: str = Column(String, nullable=True)
    customerCategory: str = Column(String, nullable=True)  # Null
    customerBizType: str = Column(String, nullable=True)  # shapes
    picName: str = Column(String, nullable=True)
    picKanaName: str = Column(String,nullable=True)  # Null
    picEmailAddress: str = Column(String, nullable=True)
    picDept: str = Column(String, nullable=True)
    picPosition: str = Column(String, nullable=True)
    sameHeadOffice: str = Column(String, nullable=True)  # Null
    contactZipCd: str = Column(String, nullable=True)
    contactAddress: str = Column(String, nullable=True)
    contactTel: str = Column(String, nullable=True)
    contactFax: str = Column(String, nullable=True)
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
    mainCustomer_1: str = Column(String, nullable=True)
    mainCustomer_2: str = Column(String, nullable=True)
    mainCustomer_3: str = Column(String, nullable=True)
    mainCustomer_4: str = Column(String, nullable=True)
    mainCustomer_5: str = Column(String, nullable=True)
    curPrdYear: str = Column(String, nullable=True)
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
    prevPrdYear: str = Column(String, nullable=True)
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
    lastPrdYear: str = Column(String, nullable=True)
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
    curPrdMainProducts: str = Column(String, nullable=True)
    mainSupplier_1: str = Column(String, nullable=True)
    mainSupplier_2: str = Column(String, nullable=True)
    mainSupplier_3: str = Column(String, nullable=True)
    mainSupplier_4: str = Column(String, nullable=True)
    mainSupplier_5: str = Column(String, nullable=True)
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
    mainProducts_1: str = Column(String, nullable=True)
    mainProducts_2: str = Column(String, nullable=True)
    mainProducts_3: str = Column(String, nullable=True)
    mainProducts_4: str = Column(String, nullable=True)
    mainProducts_5: str = Column(String, nullable=True)


    def set_data(self, xldto):
        self.customerCd: str = xldto.xlCustomerCd
        self.customerName: str = xldto.xlCustomerName
        self.customerKanaName: str = xldto.xlCustomerKanaName
        self.customerShortName: str = ""
        self.excludeLaw: bool = False
        self.headOfficeZipCd: str = xldto.xlHeadOfficeZipCd
        self.headOfficeAddress: str = xldto.xlHeadOfficeAddress
        self.headOfficeTel: str = xldto.xlHeadOfficeTel
        self.headOfficeFax: str = xldto.xlHeadOfficeFax
        self.branchOfficeZipCd: str = xldto.xlBranchOfficeZipCd
        self.branchOfficeAddress: str = xldto.xlBranchOfficeAddress
        self.branchOfficeTel: str = xldto.xlBranchOfficeTel
        self.branchOfficeFax: str = xldto.xlBranchOfficeFax
        self.repName: str = xldto.xlRepName
        self.repKanaName: str = xldto.xlRepKanaName
        self.repJobTitle: str = xldto.xlRepJobTitle
        self.repBirthday: str = YearMonthDayGenerator(xldto.xlRepBirthYear, xldto.xlRepBirthMonth,
                                                      xldto.xlRepBirthDay).year_month_day()
        self.employees: int = xldto.xlEmployees
        self.employeeYear: str = xldto.xlEmployeeYear
        self.employeeMonth: str = xldto.xlEmployeeMonth
        self.capitalForm: int = xldto.xlCapitalForm
        self.corporateType: str = xldto.xlCorporateType
        self.otherCorpType: str = ""
        self.customerCapital: float = xldto.xlCustomerCapital
        self.establishedYear: str = xldto.xlEstablishedYear
        self.establishedMonth: str = xldto.xlEstablishedMonth
        self.accountClosingMonth: int = xldto.xlAccountClosingMonth
        self.returnOnEquity: float = xldto.xlReturnOnEquity
        self.ISO9001Certif: str = ISOCertifGenerator(xldto.xlISO9001Certif, xldto.xlISO9001Plan,
                                                     xldto.xlISO9001NoCertif).certif_condition()
        self.ISO9001ResistedNo: str = xldto.xlISO9001ResistedNo
        self.ISO9001CertifPlanYM: str = YearMonthGenerator(xldto.xlISO9001CertifPlanYear,
                                                           xldto.xlISO9001CertifPlanMonth).year_month()
        self.ISO14001Certif: str = ISOCertifGenerator(xldto.xlISO14001Certif, xldto.xlISO14001Plan,
                                                      xldto.xlISO14001NoCertif).certif_condition()
        self.ISO14001ResistedNo: str = xldto.xlISO14001ResistedNo
        self.ISO14001CertifPlanYM: str = YearMonthGenerator(xldto.xlISO14001CertifPlanYear,
                                                            xldto.xlISO14001CertifPlanMonth).year_month()
        self.otherCertif: str = xldto.xlOtherCertif
        self.CustomerCategory: str = ""
        self.CustomerBizType: str = xldto.xlCustomerBizType
        self.otherBizType: str = ""
        self.picName: str = xldto.xlPicName
        self.picKanaName: str = ""
        self.PicEmailAddress: str = xldto.xlPicEmailAddress
        self.picDept: str = xldto.xlPicDept
        self.picPosition: str = xldto.xlPicPosition
        self.contactZipCd: str = xldto.xlContactZipCd
        self.contactAddress: str = xldto.xlContactAddress
        self.contactTel: str = xldto.xlContactTel
        self.contactFax: str = xldto.xlContactFax
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
        self.mainSupplier_1: str = xldto.xlMainSupplier_1
        self.mainSupplier_2: str = xldto.xlMainSupplier_2
        self.mainSupplier_3: str = xldto.xlMainSupplier_3
        self.mainSupplier_4: str = xldto.xlMainSupplier_4
        self.mainSupplier_5: str = xldto.xlMainSupplier_5
        self.mainSupplierValue_1: int = xldto.xlMainSupplierValue_1
        self.mainSupplierValue_2: int = xldto.xlMainSupplierValue_2
        self.mainSupplierValue_3: int = xldto.xlMainSupplierValue_3
        self.mainSupplierValue_4: int = xldto.xlMainSupplierValue_4
        self.mainSupplierValue_5: int = xldto.xlMainSupplierValue_5
        self.mainSupplierRatio_1: float = xldto.xlMainSupplierRatio_1
        self.mainSupplierRatio_2: float = xldto.xlMainSupplierRatio_2
        self.mainSupplierRatio_3: float = xldto.xlMainSupplierRatio_3
        self.mainSupplierRatio_4: float = xldto.xlMainSupplierRatio_4
        self.mainSupplierRatio_5: float = xldto.xlMainSupplierRatio_5
        self.mainProducts_1 = xldto.xlMainProducts_1
        self.mainProducts_2 = xldto.xlMainProducts_2
        self.mainProducts_3 = xldto.xlMainProducts_3
        self.mainProducts_4 = xldto.xlMainProducts_4
        self.mainProducts_5 = xldto.xlMainProducts_5












