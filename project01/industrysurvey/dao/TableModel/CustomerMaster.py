from dao.BaseEngine import MetaBase
from sqlalchemy import Column, Integer, String, Float, Boolean, Text
from sqlalchemy.orm import relationship
from dao.DAOFunction import YearMonthGenerator, YearMonthDayGenerator, ISOCertifGenerator


class CustomerMaster(MetaBase):
    __tablename__ = "customermaster"
    customerCd: str = Column("customerCd",String, primary_key=True, nullable=False)
    customerName: str = Column(String, nullable=True)
    customerKanaName: str = Column(String, nullable=True)
    customerShortName: str = Column(String, nullable=True)  # Null
    excludeLaw: bool = Column(Boolean, nullable=True)  # False
    headOfficeZipCd: str = Column(String, nullable=True)
    headOfficeAddress: str = Column(String, nullable=True)
    headOfficeAddress2: str = Column(String,nullable=True)
    headOfficeTel: str = Column(String, nullable=True)
    headOfficeFax: str = Column(String, nullable=True)
    branchOfficeZipCd: str = Column(String, nullable=True)
    branchOfficeAddress: str = Column(String, nullable=True)
    branchOfficeAddress2: str = Column(String, nullable=True)
    branchOfficeTel: str = Column(String, nullable=True)
    branchOfficeFax: str = Column(String, nullable=True)
    repName: str = Column(String, nullable=True)
    repKanaName: str = Column(String, nullable=True)
    repJobTitle: str = Column(String, nullable=True)
    repBirthday: str = Column(String, nullable=True)
    employees: int = Column(Integer, nullable=True)
    employeeMonth: str = Column(String, nullable=True)
    employeeYear: str = Column(String, nullable=True)
    capitalForm: str = Column(String, nullable=True)
    corporateType: str = Column(String, nullable=True)  # shapes 株式 有限 その他
    otherCorpType: str = Column(String, nullable=True)  # Null
    customerCapital: float = Column(Float)
    establishedMonth: str = Column(String, nullable=True)
    establishedYear: str = Column(String, nullable=True)
    accountClosingMonth: int = Column(Integer)
    returnOnEquity: float = Column(Float)
    ISO9001Certif: str = Column(String, nullable=True)
    ISO9001ResistedNo: str = Column(String, nullable=True)
    ISO9001CertifPlanYM: str = Column(String, nullable=True)
    ISO14001Certif: str = Column(String, nullable=True)
    ISO14001ResistedNo: str = Column(String, nullable=True)
    ISO14001CertifPlanYM: str = Column(String, nullable=True)
    otherCertif: str = Column(String, nullable=True)
    CustomerCategory: str = Column(String, nullable=True)  # Null
    CustomerBizType: str = Column(String, nullable=True)  # shapes
    otherBizType: str = Column(String, nullable=True)  # Null
    picName: str = Column(String, nullable=True)
    picKanaName: str = Column(String, nullable=True)
    PicEmailAddress: str = Column(String, nullable=True)
    picDept: str = Column(String, nullable=True)
    picPosition: str = Column(String, nullable=True)
    sameHeadOffice: str = Column(String, nullable=True)
    contactZipCd: str = Column(String, nullable=True)
    contactAddress: str = Column(String, nullable=True)
    contactTel: str = Column(String, nullable=True)
    contactFax: str = Column(String, nullable=True)

    bizconditions = relationship("BizConditionsMaster", uselist=False, backref="customermaster", cascade="all, delete-orphan")
    stockstatus = relationship("StockStatusMaster", uselist=False, backref="customermaster", cascade="all, delete-orphan")
    mainproduct = relationship("MainProductMaster", uselist=False, backref="customermaster", cascade="all, delete-orphan")
    mainsupplier = relationship("MainSupplierMaster", uselist=False, backref="customermaster", cascade="all, delete-orphan")


    def set_data(self, xldto):
        self.customerCd: str = xldto.xlCustomerCd
        self.customerName: str = xldto.xlCustomerName
        self.customerKanaName: str = xldto.xlCustomerKanaName
        self.customerShortName: str = ""
        self.excludeLaw: bool = False
        self.headOfficeZipCd: str = xldto.xlHeadOfficeZipCd
        self.headOfficeAddress: str = xldto.xlHeadOfficeAddress
        self.headOfficeAddress2: str = ""
        self.headOfficeTel: str = xldto.xlHeadOfficeTel
        self.headOfficeFax: str = xldto.xlHeadOfficeFax
        self.branchOfficeZipCd: str = xldto.xlBranchOfficeZipCd
        self.branchOfficeAddress: str = xldto.xlBranchOfficeAddress
        self.branchOfficeAddress2: str = ""
        self.branchOfficeTel: str = xldto.xlBranchOfficeTel
        self.branchOfficeFax: str = xldto.xlBranchOfficeFax
        self.repName: str = xldto.xlRepName
        self.repKanaName: str = xldto.xlRepKanaName
        self.repJobTitle: str = xldto.xlRepJobTitle
        self.repBirthday: str = YearMonthDayGenerator(xldto.xlRepBirthYear , xldto.xlRepBirthMonth, xldto.xlRepBirthDay).year_month_day()
        self.employees: int = xldto.xlEmployees
        self.employeeYear: str = xldto.xlEmployeeYear
        self.employeeMonth: str = xldto.xlEmployeeMonth
        self.capitalForm: str = xldto.xlCapitalForm
        self.corporateType: str = xldto.xlCorporateType
        self.otherCorpType: str = ""
        self.customerCapital:float = xldto.xlCustomerCapital
        self.establishedYear: str = xldto.xlEstablishedYear
        self.establishedMonth: str = xldto.xlEstablishedMonth
        self.accountClosingMonth:int = xldto.xlAccountClosingMonth
        self.returnOnEquity: float = xldto.xlReturnOnEquity
        self.ISO9001Certif: str = ISOCertifGenerator(xldto.xlISO9001Certif, xldto.xlISO9001Plan,
                                                     xldto.xlISO9001NoCertif).certif_condition()
        self.ISO9001ResistedNo: str =xldto.xlISO9001ResistedNo
        self.ISO9001CertifPlanYM: str = YearMonthGenerator(xldto.xlISO9001CertifPlanYear,
                                                           xldto.xlISO9001CertifPlanMonth).year_month()
        self.ISO14001Certif: str = ISOCertifGenerator(xldto.xlISO14001Certif, xldto.xlISO14001Plan,
                                                      xldto.xlISO14001NoCertif).certif_condition()
        self.ISO14001ResistedNo: str = xldto.xlISO14001ResistedNo
        self.ISO14001CertifPlanYM: str = YearMonthGenerator(xldto.xlISO14001CertifPlanYear,
                                                            xldto.xlISO14001CertifPlanMonth).year_month()
        self.otherCertif: str =xldto.xlOtherCertif
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
