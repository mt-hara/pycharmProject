from dao.BaseEngine import MetaBase
from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.orm import relationship


class CustomerMaster(MetaBase):
    __tablename__ = "customermaster"
    customerCd: str = Column(String, primary_key=True, nullable=False)
    customerName: str = Column(String, nullable=True)
    customerKanaName: str = Column(String, nullable=True)
    customerShortName: str = Column(String, nullable=True)  # Null
    excludeLaw: bool = Column(Boolean, nullable=True)  # False
    headOfficeZipCd: str = Column(String, nullable=True)
    headOfficeAddress: str = Column(String, nullable=True)
    headOfficeTel: str = Column(String, nullable=True)
    headOfficeFax: str = Column(String, nullable=True)
    branchOfficeZipCd: str = Column(String, nullable=True)
    branchOfficeAddress: str = Column(String, nullable=True)
    branchOfficeTel: str = Column(String, nullable=True)
    branchOfficeFax: str = Column(String, nullable=True)
    repName: str = Column(String, nullable=True)
    repKanaName: str = Column(String, nullable=True)
    repJobTitle: str = Column(String, nullable=True)
    repBirthday: str = Column(String, nullable=True)
    employees: int = Column(Integer, nullable=True)
    employeeMonth: str = Column(String, nullable=True)
    employeeYear: str = Column(String, nullable=True)
    capitalForm: int = Column(Integer, nullable=True)
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
        self.headOfficeTel: str = xldto.xlHeadOfficeTel
        self.headOfficeFax: str = xldto.xlHeadOfficeFax
        self.branchOfficeZipCd: str = xldto.xlBranchOfficeZipCd
        self.branchOfficeAddress: str = xldto.xlBranchOfficeAddress
        self.branchOfficeTel: str = xldto.xlBranchOfficeTel
        self.branchOfficeFax: str = xldto.xlBranchOfficeFax
        self.repName: str = xldto.xlRepName
        self.repKanaName: str = xldto.xlRepKanaName
        self.repJobTitle: str = xldto.xlRepJobTitle
        self.repBirthday: str = ""


    def year_month(self,year, month):
        pass


























