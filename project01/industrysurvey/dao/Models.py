from sqlalchemy import Column, Integer, String, Float, Boolean, Numeric, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class CustomerData(Base):
    __tablename__ = 'customerData'
    customerCd = Column(String, primary_key=True)
    customerName = Column(String)
    fld1 = Column(Float)


class StockStatusMaster(Base):
    __tablename__ = "StockStatusMaster"
    CustomerCd = Column(String, primary_key=True)
    stockListingStatus = Column(String)
    MainStockholder_1 = Column(String)
    MainStockholder_2 = Column(String)
    MainStockholder_3 = Column(String)
    MainStockholder_4 = Column(String)
    MainStockholder_5 = Column(String)

    AllCustomnerCd = Column(String, ForeignKey('AllCustomerMaster.CustomerCd'))
    # ratioSH_1 REAL
    # ratioSH_2 REAL
    # ratioSH_3 REAL
    # ratioSH_4 REAL
    # ratioSH_5 REAL

class AllCustomerMaster(Base):
    __tablename__ = 'AllCustomerMaster'
    CustomerCd = Column(String, primary_key=True)
    CustomerName = Column(String)
    CustomerKanaName = Column(String)
    CustomerShortName = Column(String)



    def __init__(self, xldto):
        self.CustomerCd = xldto.xlCustomerCd
        self.CustomerName =xldto.xlCustomerName




# CustomerShortName	TEXT
# excludeLaw	NUMERIC
# headOfficeZipCd	TEXT
# headOfficeAddress1	TEXT
# headOfficeAddress2	TEXT
# headOfficeTel	TEXT
# headOfficeFax	TEXT
# BranchOfficeZipCd	TEXT
# BranchOfficeAddress1	TEXT
# BranchOfficeAddress2	TEXT
# BranchOfficeTel	TEXT
# BranchOfficeFax	TEXT
# repName	TEXT
# repKanaName	TEXT
# repJobTitle	TEXT
# repBirthday	TEXT
# employees	NUMERIC
# employeeMonth	TEXT
# employeeYear	TEXT
# CapitalForm	INTEGER
# CorporateType	TEXT
# OtherCorpType	TEXT
# CustomerCapital	REAL
# establishedMonth	TEXT
# establishedYear	TEXT
# AccountClosingMonth	INTEGER
# ReturnOnEquity	REAL
# ISO9001Certif	TEXT
# ISO9001ResistedNo	TEXT
# ISO9001CertifPlanYM	TEXT
# ISO14001Certif	TEXT
# ISO14001ResistedNo	TEXT
# ISO14001CertifPlanYM	TEXT
# OtherCertif	TEXT
# CustomerCategory	TEXT
# CustomerBizType	TEXT
# picName	TEXT
# picKanaName	TEXT
# PicEmailAddress	TEXT
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
# MainStockholder_1	TEXT
# MainStockholder_2	TEXT
# MainStockholder_3	TEXT
# MainStockholder_4	TEXT
# MainStockholder_5	TEXT
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
# CurPrdYear	TEXT
# CurPrdSales_1	NUMERIC
# CurPrdSales_2	NUMERIC
# CurPrdSales_3	NUMERIC
# CurPrdSales_4	NUMERIC
# CurPrdSales_5	NUMERIC
# CurPrdSales_Our	NUMERIC
# CurPrdSales_Other	NUMERIC
# CurPrdSalesRatio_1	REAL
# CurPrdSalesRatio_2	REAL
# CurPrdSalesRatio_3	REAL
# CurPrdSalesRatio_4	REAL
# CurPrdSalesRatio_5	REAL
# CurPrdSalesRatio_Our	REAL
# CurPrdSalesRatio_Othor	REAL
# CurPrdSales_Sum	NUMERIC
# CurPrdOperatingProfit	NUMERIC
# CurPrdOrdinaryincome	NUMERIC
# PrevPrdYear	TEXT
# PrevPrdSales_1	NUMERIC
# PrevPrdSales_2	NUMERIC
# PrevPrdSales_3	NUMERIC
# PrevPrdSales_4	NUMERIC
# PrevPrdSales_5	NUMERIC
# PrevPrdSales_Our	NUMERIC
# PrevPrdSales_Other	NUMERIC
# PrevPrdSalesRatio_1	REAL
# PrevPrdSalesRatio_2	REAL
# PrevPrdSalesRatio_3	REAL
# PrevPrdSalesRatio_4	REAL
# PrevPrdSalesRatio_5	REAL
# PrevPrdSalesRatio_Our	REAL
# PrevPrdSalesRatio_Other	REAL
# PrevPrdSales_Sum	NUMERIC
# PrevPrdOperatingProfit	NUMERIC
# PrevPrdOrdinaryIncome	NUMERIC
# LastPrdYear	TEXT
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
# CurPrdMainProducts	TEXT
# MainSupplier_1	TEXT
# MainSupplier_2	TEXT
# MainSupplier_3	TEXT
# MainSupplier_4	TEXT
# MainSupplier_5	TEXT
# MainSupplierValue_1	NUMERIC
# MainSupplierValue_2	NUMERIC
# MainSupplierValue_3	NUMERIC
# MainSupplierValue_4	NUMERIC
# MainSupplierValue_5	NUMERIC
# MainSupplierRatio_1	REAL
# MainSupplierRatio_2	REAL
# MainSupplierRatio_3	REAL
# MainSupplierRatio_4	REAL
# MainSupplierRatio_5	REAL
# MainProducts_1	TEXT
# MainProducts_2	TEXT
# MainProducts_3	TEXT
# MainProducts_4	TEXT
# MainProducts_5	TEXT