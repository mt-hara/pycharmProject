from dataclasses import dataclass

@dataclass
class ShapesDataClass:
    biz_type: int = 0
    capital_form: int = 0
    corp_type: int = 0
    stock_status: bool = False
    stock_market: str = ""
    iso9000: str = ""
    iso14000: str =""

# @dataclass
# class AbsCustomerMasterDTO:
#     CustomerCd: str
#     ringNo: str
#     CustomerName: str
#     CustomerKanaName: str
#     CustomerShortName: str
#     excludeLaw: bool
#     headOfficeZipCd: str
#     headOfficeAddress1: str
#     headOfficeAddress2: str
#     headOfficeTel: str
#     headOfficeFax: str
#     BranchOfficeZipCd: str
#     BranchOfficeAddress1: str
#     BranchOfficeAddress2: str
#     BranchOfficeTel: str
#     BranchOfficeFax: str
#     repName: str
#     repKanaName: str
#     repJobTitle: str
#     repBirthday: str
#     employees: int
#     employeeMonth: int
#     employeeYear: int
#     CapitalForm: int
#     CorporateType: int
#     OtherCorpType: str
#     stockMarket: str
#     establishedMonth: int
#     establishedYear: int
#     AccountClosingMonth: int
#     ReturnOnEquity: float
#     ISO9001Certif: str
#     ISO9001ResistedNo: str
#     ISO9001CertifPlanYM: str
#     ISO14001Certif: str
#     ISO14001ResistedNo: str
#     ISO14001CertifPlanYM: str
#     OtherCertif: str
#     CustomerCategory: str
#     CustomerBizType: int
#     picName: str
#     picKanaName: str
#     PicEmailAddress: str
#     picDept: str
#     picPosition: str
#     sameHeadOffice: bool
#     contactZipCd: str
#     contactAddress1: str
#     contactAddress2: str
#     contactTel: str
#     contactFax: str
#     contactInfo: str
#

@dataclass
class AbstractAllCustomerMaster:
    CustomerCd: str
    ringiNo: str
    CustomerName: str
    CustomerKanaName: str
    CustomerShortName: str
    excludeLaw: bool
    headOfficeZipCd: str
    headOfficeAddress1: str
    headOfficeAddress2: str
    headOfficeTel: str
    headOfficeFax: str
    BranchOfficeZipCd: str
    BranchOfficeAddress1: str
    BranchOfficeAddress2: str
    BranchOfficeTel: str
    BranchOfficeFax: str
    repName: str
    repKanaName: str
    repJobTitle: str
    repBirthday: str
    employees: int
    employeeMonth: int
    employeeYear: int
    CapitalForm: int    # shape 取得
    CorporateType: str  # shape 取得
    OtherCorpType: str
    CustomerCapital: float
    establishedMonth: int
    establishedYear: int
    AccountClosingMonth: int
    ReturnOnEquity: float
    ISO9001Certif: str  #shape 取得 取得済 取得予定 取得予定なし
    ISO9001ResistedNo: str
    ISO9001CertifPlanYM: str
    ISO14001Certif: str #shape 取得 取得 取得済 取得予定 取得予定なし
    ISO14001ResistedNo: str
    ISO14001CertifPlanYM: str
    OtherCertif: str
    CustomerCategory: str
    CustomerBizType: int    #shape 取得
    picName: str
    picKanaName: str
    PicEmailAddress: str
    picDept: str
    picPosition: str
    sameHeadOffice: str
    contactZipCd: str
    contactAddress1: str
    contactAddress2: str
    contactTel: str
    contactFax: str
    contactInfo: str
    FTA: int  # 1:取引基本契約書 締結済
    FTANotice: str
    QAA: int  # 1:品質保証協定書 締結済
    QAANotice: str
    NDA: int  # 1:秘密保持契約書 締結済
    NDANotice: str
    otherContract: str
    stockListingStatus: bool  # 0:非上場　1:上場 shape 取得
    stockMarket: str    # shape 取得 Text
    MainStockholder_1: str
    MainStockholder_2: str
    MainStockholder_3: str
    MainStockholder_4: str
    MainStockholder_5: str
    ratioSH_1: float
    ratioSH_2: float
    ratioSH_3: float
    ratioSH_4: float
    ratioSH_5: float
    mainCustomer_1: str
    mainCustomer_2: str
    mainCustomer_3: str
    mainCustomer_4: str
    mainCustomer_5: str
    CurPrdYear: str
    CurPrdSales_1: float
    CurPrdSales_2: float
    CurPrdSales_3: float
    CurPrdSales_4: float
    CurPrdSales_5: float
    CurPrdSales_Our: float
    CurPrdSales_Other: float
    CurPrdSalesRatio_1: float
    CurPrdSalesRatio_2: float
    CurPrdSalesRatio_3: float
    CurPrdSalesRatio_4: float
    CurPrdSalesRatio_5: float
    CurPrdSalesRatio_Our: float
    CurPrdSalesRatio_Othor: float
    CurPrdSales_Sum: float
    CurPrdOperatingProfit: float
    CurPrdOrdinaryincome: float
    PrevPrdYear: str
    PrevPrdSales_1: float
    PrevPrdSales_2: float
    PrevPrdSales_3: float
    PrevPrdSales_4: float
    PrevPrdSales_5: float
    PrevPrdSales_Our: float
    PrevPrdSales_Other: float
    PrevPrdSalesRatio_1: float
    PrevPrdSalesRatio_2: float
    PrevPrdSalesRatio_3: float
    PrevPrdSalesRatio_4: float
    PrevPrdSalesRatio_5: float
    PrevPrdSalesRatio_Our: float
    PrevPrdSalesRatio_Other: float
    PrevPrdSales_Sum: float
    PrevPrdOperatingProfit: float
    PrevPrdOrdinaryIncome: float
    LastPrdYear: str
    lastPrdSales_1: float
    lastPrdSales_2: float
    lastPrdSales_3: float
    lastPrdSales_4: float
    lastPrdSales_5: float
    lastPrdSales_Our: float
    lastPrdSales_Other: float
    lastPrdSalesRatio_1: float
    lastPrdSalesRatio_2: float
    lastPrdSalesRatio_3: float
    lastPrdSalesRatio_4: float
    lastPrdSalesRatio_5: float
    lastPrdSalesRatio_Our: float
    lastPrdSalesRatio_Other: float
    lastPrdSales_sum: float
    lastPrdOperatingProfit: float
    lastPrdOrdinaryincome: float
    CurPrdMainProducts: str
    MainSupplier_1: str
    MainSupplier_2: str
    MainSupplier_3: str
    MainSupplier_4: str
    MainSupplier_5: str
    MainSupplierValue_1: float
    MainSupplierValue_2: float
    MainSupplierValue_3: float
    MainSupplierValue_4: float
    MainSupplierValue_5: float
    MainSupplierRatio_1: float
    MainSupplierRatio_2: float
    MainSupplierRatio_3: float
    MainSupplierRatio_4: float
    MainSupplierRatio_5: float
    MainProducts_1: str
    MainProducts_2: str
    MainProducts_3: str
    MainProducts_4: str
    MainProducts_5: str
