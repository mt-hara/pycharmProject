from dao.BaseEngine import MetaBase
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship

Base = MetaBase

class CustomerMaster(Base):
    __tablename__ = "customermaster"
    customerCd: str = Column(String, primary_key=True, nullable=False)
    customerName: str = Column(String, nullable=True)
    customerKanaName: str = Column(String, nullable=True)
    customerShortName: str = Column(String, nullable=True)
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

    stockstatus = relationship("StockStatusMaster", uselist=False, backref="customermaster", cascade="all, delete-orphan")

    def set_data(self,xldto):
        self.customerCd = xldto.xlCustomerCd
        self.customerName = xldto.xlCustomerName
