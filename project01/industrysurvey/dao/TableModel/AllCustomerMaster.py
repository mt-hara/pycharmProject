from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class AllCustomerMaster(Base):
    __tablename__ = "allcustomermaster"
    customerCd: str = Column(String, primary_key=True, nullable=False)
    customerName: str = Column(String, nullable=True)
    customerKanaName: str = Column(String, nullable=True)
    customerShortName: str = Column(String, nullable=True)
    excludeLaw: bool = Column(Boolean)  # False
    headOfficeZipCd: str = Column(String, nullable=True)
    headOfficeAddress: str = Column(String, nullable=True)
    headOfficeTel: str = Column(String, nullable=True)
    headOfficeFax:str = Column(String, nullable=True)
    branchOfficeZipCd: str = Column(String, nullable=True)
    branchOfficeAddress: str = Column(String, nullable=True)
    branchOfficeTel: str = Column(String, nullable=True)
    branchOfficeFax: str = Column(String, nullable=True)


# 	TEXT
# branchOfficeZipCd	TEXT
# branchOfficeAddress1	TEXT
# branchOfficeAddress2	TEXT
# branchOfficeTel	TEXT
# branchOfficeFax	TEXT
# repName	TEXT
# repKanaName	TEXT
# repJobTitle	TEXT
# repBirthday	TEXT
# employees	NUMERIC
# employeeMonth	TEXT
# employeeYear	TEXT
# capitalForm	INTEGER
# corporateType	TEXT
# otherCorpType	TEXT
# customerCapital	REAL
# establishedMonth	TEXT
# establishedYear	TEXT
# accountClosingMonth	INTEGER
# returnOnEquity	REAL
# ISO9001Certif	TEXT
# ISO9001ResistedNo	TEXT
# ISO9001CertifPlanYM	TEXT
# ISO14001Certif	TEXT
# ISO14001ResistedNo	TEXT
# ISO14001CertifPlanYM	TEXT
# otherCertif	TEXT
# customerCategory	TEXT
# customerBizType	TEXT
# picName	TEXT
# picKanaName	TEXT
# picEmailAddress	TEXT
# picDept	TEXT
# picPosition	TEXT
# sameHeadOffice	TEXT
# contactZipCd	TEXT
# contactAddress1	TEXT
# contactAddress2	TEXT
# contactTel	TEXT
# contactFax	TEXT
# contactInfo	TEXT
# FTA	NUMERIC
# FTANotice	TEXT
# QAA	NUMERIC
# QAANotice	TEXT
# NDA	NUMERIC
# NDANotice	TEXT
# otherContract	TEXT
# stockListingStatus	NUMERIC
# stockMarket	TEXT
# mainStockholder_1	TEXT
# mainStockholder_2	TEXT
# mainStockholder_3	TEXT
# mainStockholder_4	TEXT
# mainStockholder_5	TEXT
# ratioSH_1	REAL
# ratioSH_2	REAL
# ratioSH_3	REAL
# ratioSH_4	REAL
# ratioSH_5	REAL
# mainCustomer_1	TEXT
# mainCustomer_2	TEXT
# mainCustomer_3	TEXT
# mainCustomer_4	TEXT
# mainCustomer_5	TEXT
# curPrdYear	TEXT
# curPrdSales_1	NUMERIC
# curPrdSales_2	NUMERIC
# curPrdSales_3	NUMERIC
# curPrdSales_4	NUMERIC
# curPrdSales_5	NUMERIC
# curPrdSales_Our	NUMERIC
# curPrdSales_Other	NUMERIC
# curPrdSalesRatio_1	REAL
# curPrdSalesRatio_2	REAL
# curPrdSalesRatio_3	REAL
# curPrdSalesRatio_4	REAL
# curPrdSalesRatio_5	REAL
# curPrdSalesRatio_Our	REAL
# curPrdSalesRatio_Othor	REAL
# curPrdSales_Sum	NUMERIC
# curPrdOperatingProfit	NUMERIC
# curPrdOrdinaryincome	NUMERIC
# prevPrdYear	TEXT
# prevPrdSales_1	NUMERIC
# prevPrdSales_2	NUMERIC
# prevPrdSales_3	NUMERIC
# prevPrdSales_4	NUMERIC
# prevPrdSales_5	NUMERIC
# prevPrdSales_Our	NUMERIC
# prevPrdSales_Other	NUMERIC
# prevPrdSalesRatio_1	REAL
# prevPrdSalesRatio_2	REAL
# prevPrdSalesRatio_3	REAL
# prevPrdSalesRatio_4	REAL
# prevPrdSalesRatio_5	REAL
# prevPrdSalesRatio_Our	REAL
# prevPrdSalesRatio_Other	REAL
# prevPrdSales_Sum	NUMERIC
# prevPrdOperatingProfit	NUMERIC
# prevPrdOrdinaryIncome	NUMERIC
# lastPrdYear	TEXT
# lastPrdSales_1	NUMERIC
# lastPrdSales_2	NUMERIC
# lastPrdSales_3	NUMERIC
# lastPrdSales_4	NUMERIC
# lastPrdSales_5	NUMERIC
# lastPrdSales_Our	NUMERIC
# lastPrdSales_Other	NUMERIC
# lastPrdSalesRatio_1	REAL
# lastPrdSalesRatio_2	REAL
# lastPrdSalesRatio_3	REAL
# lastPrdSalesRatio_4	REAL
# lastPrdSalesRatio_5	REAL
# lastPrdSalesRatio_Our	REAL
# lastPrdSalesRatio_Other	REAL
# lastPrdSales_sum	NUMERIC
# lastPrdOperatingProfit	NUMERIC
# lastPrdOrdinaryincome	NUMERIC
# curPrdMainProducts	TEXT
# mainSupplier_1	TEXT
# mainSupplier_2	TEXT
# mainSupplier_3	TEXT
# mainSupplier_4	TEXT
# mainSupplier_5	TEXT
# mainSupplierValue_1	NUMERIC
# mainSupplierValue_2	NUMERIC
# mainSupplierValue_3	NUMERIC
# mainSupplierValue_4	NUMERIC
# mainSupplierValue_5	NUMERIC
# mainSupplierRatio_1	REAL
# mainSupplierRatio_2	REAL
# mainSupplierRatio_3	REAL
# mainSupplierRatio_4	REAL
# mainSupplierRatio_5	REAL
# mainProducts_1	TEXT
# mainProducts_2	TEXT
# mainProducts_3	TEXT
# mainProducts_4	TEXT
# mainProducts_5	TEXT