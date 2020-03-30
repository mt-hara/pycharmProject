from dataclasses import dataclass


@dataclass
class ShapesDataClass:
    biz_type: int = None
    capital_form: int = None
    corp_type: int = None
    stock_status: bool = None
    stock_market: str = ""
    iso9000: str = ""
    iso14000: str = ""

@dataclass
class DataCls:
    __customerCd: str

    @property
    def customerCd(self):
        return self.__customerCd

    @customerCd.setter
    def customerCd(self, param):
        self.__customerCd = param






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
class CustomerMaster:
    CustomerCd: str = ""  # H3
    ringiNo: str = ""  # ""
    CustomerName: str = ""  # H5
    CustomerKanaName: str = ""  # H4
    CustomerShortName: str = ""  # ""
    excludeLaw: bool = False  # false
    headOfficeZipCd: str = ""  # I7
    headOfficeAddress1: str = ""  # H8
    headOfficeAddress2: str = ""  # ""
    headOfficeTel: str = ""  # X7
    headOfficeFax: str = ""  # AH7
    BranchOfficeZipCd: str = ""  # I10
    BranchOfficeAddress1: str = ""  # H11
    BranchOfficeAddress2: str = ""  # ""
    BranchOfficeTel: str = ""  # X10
    BranchOfficeFax: str = ""  # AH10
    repName: str = ""  # H14
    repKanaName: str = ""  # H13
    repJobTitle: str = ""  # AD13
    repBirthday: str = ""  # AD14 + "年" + AH14 + "月" + AK14 + "日"
    employees: int = 0  # k22
    employeeMonth: int = 0  # I23
    employeeYear: int = 0  # O23
    CapitalForm: int = 0  # shape 取得
    CorporateType: str = ""  # shape 取得
    OtherCorpType: str = ""  # ""
    CustomerCapital: float = 0  # H18
    establishedMonth: int = 0  # I19
    establishedYear: int = 0  # O19
    AccountClosingMonth: int = 0  # M21
    ReturnOnEquity: float = 0  # I20
    ISO9001Certif: str = ""  # D50 shape 取得 取得済 取得予定 取得予定なし
    ISO9001ResistedNo: str = ""  # N50
    ISO9001CertifPlanYM: str = ""  # N51 + "年" + R51 "月"
    ISO14001Certif: str = ""  # V50 shape 取得 取得 取得済 取得予定 取得予定なし
    ISO14001ResistedNo: str = ""  # AF50
    ISO14001CertifPlanYM: str = ""  # AF51 + "年" + AJ51 "月"
    OtherCertif: str = ""  # I53
    CustomerCategory: str = ""  # ""
    CustomerBizType: int = 0  # shape 取得
    picName: str = ""  # H57
    picKanaName: str = ""  # ""
    PicEmailAddress: str = ""  # H58
    picDept: str = ""  # H59
    picPosition: str = ""  # G59
    sameHeadOffice: str = ""  # ""
    contactZipCd: str = ""  # H55
    contactAddress1: str = ""  # C56
    contactAddress2: str = ""  # ""
    contactTel: str = ""  # H60
    contactFax: str = ""  # G60
    contactInfo: str = ""  # ""
    FTA: int = 0  # 0 1:取引基本契約書 締結済
    FTANotice: str = ""  # ""
    QAA: int = 0  # 0 1:品質保証協定書 締結済
    QAANotice: str = ""  # ""
    NDA: int = 0  # 0 1:秘密保持契約書 締結済
    NDANotice: str = ""  # ""
    otherContract: str = ""  # ""
    stockListingStatus: int = 0  # 0:非上場　1:上場 shape 取得
    stockMarket: str = ""  # shape 取得 Text
    MainStockholder_1: str = ""  # U19
    MainStockholder_2: str = ""  # U20
    MainStockholder_3: str = ""  # U21
    MainStockholder_4: str = ""  # U22
    MainStockholder_5: str = ""  # U23
    ratioSH_1: float = 0  # AK19
    ratioSH_2: float = 0  # AK20
    ratioSH_3: float = 0  # AK21
    ratioSH_4: float = 0  # AK22
    ratioSH_5: float = 0  # AK23
    mainCustomer_1: str = ""  # C28
    mainCustomer_2: str = ""  # C29
    mainCustomer_3: str = ""  # C30
    mainCustomer_4: str = ""  # C31
    mainCustomer_5: str = ""  # C32
    CurPrdYear: str = ""  # M26
    CurPrdSales_1: float = 0  # M28
    CurPrdSales_2: float = 0  # M29
    CurPrdSales_3: float = 0  # M30
    CurPrdSales_4: float = 0  # M31
    CurPrdSales_5: float = 0  # M32
    CurPrdSales_Our: float = 0  # M34
    CurPrdSales_Other: float = 0  # M33
    CurPrdSalesRatio_1: float = 0  # S28
    CurPrdSalesRatio_2: float = 0  # S29
    CurPrdSalesRatio_3: float = 0  # S30
    CurPrdSalesRatio_4: float = 0  # S31
    CurPrdSalesRatio_5: float = 0  # S32
    CurPrdSalesRatio_Our: float = 0  # S34
    CurPrdSalesRatio_Othor: float = 0  # S33
    CurPrdSales_Sum: float = 0  # M35
    CurPrdOperatingProfit: float = 0  # M36
    CurPrdOrdinaryincome: float = 0  # M37
    PrevPrdYear: str = ""  # V26
    PrevPrdSales_1: float = 0  # V28
    PrevPrdSales_2: float = 0  # V29
    PrevPrdSales_3: float = 0  # V30
    PrevPrdSales_4: float = 0  # V31
    PrevPrdSales_5: float = 0  # V32
    PrevPrdSales_Our: float = 0  # V34
    PrevPrdSales_Other: float = 0  # V33
    PrevPrdSalesRatio_1: float = 0  # AB28
    PrevPrdSalesRatio_2: float = 0  # AB29
    PrevPrdSalesRatio_3: float = 0  # AB30
    PrevPrdSalesRatio_4: float = 0  # AB31
    PrevPrdSalesRatio_5: float = 0  # AB32
    PrevPrdSalesRatio_Our: float = 0  # AB34
    PrevPrdSalesRatio_Other: float = 0 # AB33
    PrevPrdSales_Sum: float = 0  # V35
    PrevPrdOperatingProfit: float = 0  # V36
    PrevPrdOrdinaryIncome: float = 0  # V37
    LastPrdYear: str = ""  # AE26
    lastPrdSales_1: float = 0  # AE28
    lastPrdSales_2: float = 0  # AE29
    lastPrdSales_3: float = 0  # AE30
    lastPrdSales_4: float = 0  # AE31
    lastPrdSales_5: float = 0  # AE32
    lastPrdSales_Our: float = 0  # AE34
    lastPrdSales_Other: float = 0  # AE33
    lastPrdSalesRatio_1: float = 0  # AK28
    lastPrdSalesRatio_2: float = 0  # AK29
    lastPrdSalesRatio_3: float = 0  # AK30
    lastPrdSalesRatio_4: float = 0  # AK31
    lastPrdSalesRatio_5: float = 0  # AK32
    lastPrdSalesRatio_Our: float = 0  # AK34
    lastPrdSalesRatio_Other: float = 0  # AK33
    lastPrdSales_sum: float = 0  # AE35
    lastPrdOperatingProfit: float = 0  # AE36
    lastPrdOrdinaryincome: float = 0  # AE37
    CurPrdMainProducts: str = ""  # M38
    MainSupplier_1: str = ""  # W42
    MainSupplier_2: str = ""  # W43
    MainSupplier_3: str = ""  # W44
    MainSupplier_4: str = ""  # W45
    MainSupplier_5: str = ""  # W46
    MainSupplierValue_1: float = 0  # AG42
    MainSupplierValue_2: float = 0  # AG43
    MainSupplierValue_3: float = 0  # AG44
    MainSupplierValue_4: float = 0  # AG45
    MainSupplierValue_5: float = 0  # AG46
    MainSupplierRatio_1: float = 0  # AK42
    MainSupplierRatio_2: float = 0  # AK43
    MainSupplierRatio_3: float = 0  # AK44
    MainSupplierRatio_4: float = 0  # AK45
    MainSupplierRatio_5: float = 0  # AK46
    MainProducts_1: str = ""  # C42
    MainProducts_2: str = ""  # C43
    MainProducts_3: str = ""  # C44
    MainProducts_4: str = ""  # C45
    MainProducts_5: str = ""  # C46

    # def set_shapes_data(self,fieldname,data):
    #     if fieldname == "CustomerBizType":
    #         self.CustomerBizType = data
    #     elif fieldname == "CapitalForm":
    #         self.CapitalForm = data
    #     elif fieldname == "CorporateType":
    #         self.CorporateType = data
    #     elif fieldname == "stockListingStatus":
    #         self.stockListingStatus = data
    #     elif fieldname == "stockMarket":
    #         self.stockMarket = data
    #     elif fieldname == "ISO9001Certif":
    #         self.ISO9001Certif = data
    #     elif fieldname == "ISO14001Certif":
    #         self.ISO14001Certif = data
    #
    # def iso_certif(self,ws):
    #     self.i9000certif = ws.range("D50").value
    #     self.i9000plan = ws.range("D51").value
    #     self.i9000nocertif = ws.range("D52").value
    #     self.i14000certif = ws.range("V50").value
    #     self.i14000plan = ws.range("V51").value
    #     self.i14000nocertif = ws.range("V52").value
    #
    #     if self.ISO9001Certif == "" or self.ISO9001Certif is None:
    #         if self.i9000certif is not None:
    #             self.ISO9001Certif = "取得済"
    #         elif self.i9000plan is not None:
    #             self.ISO9001Certif = "取得予定"
    #         elif self.i9000nocertif is not None:
    #             self.ISO9001Certif = "取得予定なし"
    #
    #     if self.ISO14001Certif == "" or self.ISO14001Certif is None:
    #         if self.i14000certif is not None:
    #             self.ISO14001Certif = "取得済"
    #         elif self.i14000plan is not None:
    #             self.ISO14001Certif = "取得予定"
    #         elif self.i14000nocertif is not None:
    #             self.ISO14001Certif = "取得予定なし"
    #
    # def set_cell_data(self,ws):
    #     self.CustomerCd: str = str(ws.range("H3").value)  # H3
    #     self.ringiNo: str = ""
    #     self.CustomerName: str = str(ws.range("H5").value) # H5
    #     self.CustomerKanaName: str =str(ws.range("H4").value)  # H4
    #     self.CustomerShortName: str = ""
    #     self.excludeLaw: bool = False
    #     self.headOfficeZipCd: str = str(ws.range("I7").value)  # I7
    #     self.headOfficeAddress1: str = str(ws.range("H8").value)  # H8
    #     self.headOfficeAddress2: str = ""  # ""
    #     self.headOfficeTel: str = str(ws.range("X7").value)  # X7
    #     self.headOfficeFax: str = str(ws.range("AH7").value)  # AH7
    #     self.BranchOfficeZipCd: str = str(ws.range("I10").value)  # I10
    #     self.BranchOfficeAddress1: str = str(ws.range("H11").value)  # H11
    #     self.BranchOfficeAddress2: str = ""  # ""
    #     self.BranchOfficeTel: str = str(ws.range("X10").value)  # X10
    #     self.BranchOfficeFax: str = str(ws.range("AH10").value)  # AH10
    #     self.repName: str = str(ws.range("H14").value)  # H14
    #     self.repKanaName: str = str(ws.range("H13").value)  # H13
    #     self.repJobTitle: str = str(ws.range("AD13").value)  # AD13
    #     tmpbirthday:str = str(int(ws.range("AD14").value)) + "年" \
    #                   + str(int(ws.range("AH14").value)) + "月" +\
    #                   str(int(ws.range("AK14").value)) + "日"
    #     self.repBirthday: str = tmpbirthday  # AD14 + "年" + AH14 + "月" + AK14 + "日"
    #     self.employees: int =int(ws.range("K22").value)  # k22
    #     self.employeeMonth: int = int(ws.range("I23").value)  # I23
    #     self.employeeYear: int = int(ws.range("O23").value)  # O23
    #     # CapitalForm: int = 0  # shape 取得
    #     # CorporateType: str = ""  # shape 取得
    #     self.OtherCorpType: str = ""  # ""
    #     self.CustomerCapital: float = float(ws.range("H18").value)  # H18
    #     self.establishedMonth: int = int(ws.range("I19").value)  # I19
    #     self.establishedYear: int = int(ws.range("O19").value)  # O19
    #     self.AccountClosingMonth: int = int(ws.range("M21").value)  # M21
    #     self.ReturnOnEquity: float = float(ws.range("I20").value)  # I20
    #     self.iso_certif(ws)
    #     self.ISO9001ResistedNo: str = str(ws.range("N50").value)  # N50
    #     tmpi9000ym = str(str(ws.range("N51").value) + "年" \
    #                      + str(ws.range("R51").value) + "月")
    #     self.ISO9001CertifPlanYM: str = tmpi9000ym  # N51 + "年" + R51 "月"
    #     self.ISO14001ResistedNo: str = str(ws.range("AF50").value)  # AF50
    #     # ISO14001CertifPlanYM: str = ""  # AF51 + "年" + AJ51 "月"
    #     # OtherCertif: str = ""  # I53
    #     # CustomerCategory: str = ""  # ""
    #     # CustomerBizType: int = 0  # shape 取得
    #     # picName: str = ""  # H57
    #     # picKanaName: str = ""  # ""
    #     # PicEmailAddress: str = ""  # H58
    #     # picDept: str = ""  # H59
    #     # picPosition: str = ""  # G59
    #     # sameHeadOffice: str = ""  # ""
    #     # contactZipCd: str = ""  # H55
    #     # contactAddress1: str = ""  # C56
    #     # contactAddress2: str = ""  # ""
    #     # contactTel: str = ""  # H60
    #     # contactFax: str = ""  # G60
    #     # contactInfo: str = ""  # ""
    #     # FTA: int = 0  # 0 1:取引基本契約書 締結済
    #     # FTANotice: str = ""  # ""
    #     # QAA: int = 0  # 0 1:品質保証協定書 締結済
    #     # QAANotice: str = ""  # ""
    #     # NDA: int = 0  # 0 1:秘密保持契約書 締結済
    #     # NDANotice: str = ""  # ""
    #     # otherContract: str = ""  # ""
    #     # stockListingStatus: int = 0  # 0:非上場　1:上場 shape 取得
    #     # stockMarket: str = ""  # shape 取得 Text
    #     # MainStockholder_1: str = ""  # U19
    #     # MainStockholder_2: str = ""  # U20
    #     # MainStockholder_3: str = ""  # U21
    #     # MainStockholder_4: str = ""  # U22
    #     # MainStockholder_5: str = ""  # U23
    #     # ratioSH_1: float = 0  # AK19
    #     # ratioSH_2: float = 0  # AK20
    #     # ratioSH_3: float = 0  # AK21
    #     # ratioSH_4: float = 0  # AK22
    #     # ratioSH_5: float = 0  # AK23
    #     # mainCustomer_1: str = ""  # C28
    #     # mainCustomer_2: str = ""  # C29
    #     # mainCustomer_3: str = ""  # C30
    #     # mainCustomer_4: str = ""  # C31
    #     # mainCustomer_5: str = ""  # C32
    #     # CurPrdYear: str = ""  # M26
    #     # CurPrdSales_1: float = 0  # M28
    #     # CurPrdSales_2: float = 0  # M29
    #     # CurPrdSales_3: float = 0  # M30
    #     # CurPrdSales_4: float = 0  # M31
    #     # CurPrdSales_5: float = 0  # M32
    #     # CurPrdSales_Our: float = 0  # M34
    #     # CurPrdSales_Other: float = 0  # M33
    #     # CurPrdSalesRatio_1: float = 0  # S28
    #     # CurPrdSalesRatio_2: float = 0  # S29
    #     # CurPrdSalesRatio_3: float = 0  # S30
    #     # CurPrdSalesRatio_4: float = 0  # S31
    #     # CurPrdSalesRatio_5: float = 0  # S32
    #     # CurPrdSalesRatio_Our: float = 0  # S34
    #     # CurPrdSalesRatio_Othor: float = 0  # S33
    #     # CurPrdSales_Sum: float = 0  # M35
    #     # CurPrdOperatingProfit: float = 0  # M36
    #     # CurPrdOrdinaryincome: float = 0  # M37
    #     # PrevPrdYear: str = ""  # V26
    #     # PrevPrdSales_1: float = 0  # V28
    #     # PrevPrdSales_2: float = 0  # V29
    #     # PrevPrdSales_3: float = 0  # V30
    #     # PrevPrdSales_4: float = 0  # V31
    #     # PrevPrdSales_5: float = 0  # V32
    #     # PrevPrdSales_Our: float = 0  # V34
    #     # PrevPrdSales_Other: float = 0  # V33
    #     # PrevPrdSalesRatio_1: float = 0  # AB28
    #     # PrevPrdSalesRatio_2: float = 0  # AB29
    #     # PrevPrdSalesRatio_3: float = 0  # AB30
    #     # PrevPrdSalesRatio_4: float = 0  # AB31
    #     # PrevPrdSalesRatio_5: float = 0  # AB32
    #     # PrevPrdSalesRatio_Our: float = 0  # AB34
    #     # PrevPrdSalesRatio_Other: float = 0  # AB33
    #     # PrevPrdSales_Sum: float = 0  # V35
    #     # PrevPrdOperatingProfit: float = 0  # V36
    #     # PrevPrdOrdinaryIncome: float = 0  # V37
    #     # LastPrdYear: str = ""  # AE26
    #     # lastPrdSales_1: float = 0  # AE28
    #     # lastPrdSales_2: float = 0  # AE29
    #     # lastPrdSales_3: float = 0  # AE30
    #     # lastPrdSales_4: float = 0  # AE31
    #     # lastPrdSales_5: float = 0  # AE32
    #     # lastPrdSales_Our: float = 0  # AE34
    #     # lastPrdSales_Other: float = 0  # AE33
    #     # lastPrdSalesRatio_1: float = 0  # AK28
    #     # lastPrdSalesRatio_2: float = 0  # AK29
    #     # lastPrdSalesRatio_3: float = 0  # AK30
    #     # lastPrdSalesRatio_4: float = 0  # AK31
    #     # lastPrdSalesRatio_5: float = 0  # AK32
    #     # lastPrdSalesRatio_Our: float = 0  # AK34
    #     # lastPrdSalesRatio_Other: float = 0  # AK33
    #     # lastPrdSales_sum: float = 0  # AE35
    #     # lastPrdOperatingProfit: float = 0  # AE36
    #     # lastPrdOrdinaryincome: float = 0  # AE37
    #     # CurPrdMainProducts: str = ""  # M38
    #     # MainSupplier_1: str = ""  # W42
    #     # MainSupplier_2: str = ""  # W43
    #     # MainSupplier_3: str = ""  # W44
    #     # MainSupplier_4: str = ""  # W45
    #     # MainSupplier_5: str = ""  # W46
    #     # MainSupplierValue_1: float = 0  # AG42
    #     # MainSupplierValue_2: float = 0  # AG43
    #     # MainSupplierValue_3: float = 0  # AG44
    #     # MainSupplierValue_4: float = 0  # AG45
    #     # MainSupplierValue_5: float = 0  # AG46
    #     # MainSupplierRatio_1: float = 0  # AK42
    #     # MainSupplierRatio_2: float = 0  # AK43
    #     # MainSupplierRatio_3: float = 0  # AK44
    #     # MainSupplierRatio_4: float = 0  # AK45
    #     # MainSupplierRatio_5: float = 0  # AK46
    #     # MainProducts_1: str = ""  # C42
    #     # MainProducts_2: str = ""  # C43
    #     # MainProducts_3: str = ""  # C44
    #     # MainProducts_4: str = ""  # C45
    #     # MainProducts_5: str = ""  # C46




# @dataclass
# class AllCustomerMaster:
#     CustomerCd: str  # H3
#     ringiNo: str  #  ""
#     CustomerName: str  # H5
#     CustomerKanaName: str  # H4
#     CustomerShortName: str  # ""
#     excludeLaw: bool  # false
#     headOfficeZipCd: str  # I7
#     headOfficeAddress1: str  # H8
#     headOfficeAddress2: str  # ""
#     headOfficeTel: str  # X7
#     headOfficeFax: str  # AH7
#     BranchOfficeZipCd: str  # I10
#     BranchOfficeAddress1: str  # H11
#     BranchOfficeAddress2: str  # ""
#     BranchOfficeTel: str  # X10
#     BranchOfficeFax: str  # AH10
#     repName: str  # H14
#     repKanaName: str  # H13
#     repJobTitle: str  # AD13
#     repBirthday: str  # AD14 + "年" + AH14 + "月" + AK14 + "日"
#     employees: int  # k22
#     employeeMonth: int  # I23
#     employeeYear: int  # O23
#     CapitalForm: int  # shape 取得
#     CorporateType: str  # shape 取得
#     OtherCorpType: str  # ""
#     CustomerCapital: float  # H18
#     establishedMonth: int  # I19
#     establishedYear: int  # O19
#     AccountClosingMonth: int  # M21
#     ReturnOnEquity: float  # I20
#     ISO9001Certif: str  # D50 shape 取得 取得済 取得予定 取得予定なし
#     ISO9001ResistedNo: str  # N50
#     ISO9001CertifPlanYM: str  # N51 + "年" + R51 "月"
#     ISO14001Certif: str  # V50 shape 取得 取得 取得済 取得予定 取得予定なし
#     ISO14001ResistedNo: str  # AF50
#     ISO14001CertifPlanYM: str  # AF51 + "年" + AJ51 "月"
#     OtherCertif: str  # I53
#     CustomerCategory: str  # ""
#     CustomerBizType: int  # shape 取得
#     picName: str  # H57
#     picKanaName: str  # ""
#     PicEmailAddress: str  # H58
#     picDept: str  # H59
#     picPosition: str  # G59
#     sameHeadOffice: str  # ""
#     contactZipCd: str  # H55
#     contactAddress1: str  # C56
#     contactAddress2: str  # ""
#     contactTel: str  # H60
#     contactFax: str  # G60
#     contactInfo: str  # ""
#     FTA: int  # 0 1:取引基本契約書 締結済
#     FTANotice: str  # ""
#     QAA: int  # 0 1:品質保証協定書 締結済
#     QAANotice: str  # ""
#     NDA: int  # 0 1:秘密保持契約書 締結済
#     NDANotice: str  # ""
#     otherContract: str  # ""
#     stockListingStatus: bool  # 0:非上場　1:上場 shape 取得
#     stockMarket: str  # shape 取得 Text
#     MainStockholder_1: str  # U19
#     MainStockholder_2: str  # U20
#     MainStockholder_3: str  # U21
#     MainStockholder_4: str  # U22
#     MainStockholder_5: str  # U23
#     ratioSH_1: float  # AK19
#     ratioSH_2: float  # AK20
#     ratioSH_3: float  # AK21
#     ratioSH_4: float  # AK22
#     ratioSH_5: float  # AK23
#     mainCustomer_1: str  # C28
#     mainCustomer_2: str  # C29
#     mainCustomer_3: str  # C30
#     mainCustomer_4: str  # C31
#     mainCustomer_5: str  # C32
#     CurPrdYear: str  # M26
#     CurPrdSales_1: float  # M28
#     CurPrdSales_2: float  # M29
#     CurPrdSales_3: float  # M30
#     CurPrdSales_4: float  # M31
#     CurPrdSales_5: float  # M32
#     CurPrdSales_Our: float  # M34
#     CurPrdSales_Other: float  # M33
#     CurPrdSalesRatio_1: float  # S28
#     CurPrdSalesRatio_2: float  # S29
#     CurPrdSalesRatio_3: float  # S30
#     CurPrdSalesRatio_4: float  # S31
#     CurPrdSalesRatio_5: float  # S32
#     CurPrdSalesRatio_Our: float  # S34
#     CurPrdSalesRatio_Othor: float  # S33
#     CurPrdSales_Sum: float  # M35
#     CurPrdOperatingProfit: float  # M36
#     CurPrdOrdinaryincome: float  # M37
#     PrevPrdYear: str  # V26
#     PrevPrdSales_1: float  # V28
#     PrevPrdSales_2: float  # V29
#     PrevPrdSales_3: float  # V30
#     PrevPrdSales_4: float  # V31
#     PrevPrdSales_5: float  # V32
#     PrevPrdSales_Our: float  # V34
#     PrevPrdSales_Other: float  # V33
#     PrevPrdSalesRatio_1: float  # AB28
#     PrevPrdSalesRatio_2: float  # AB29
#     PrevPrdSalesRatio_3: float  # AB30
#     PrevPrdSalesRatio_4: float  # AB31
#     PrevPrdSalesRatio_5: float  # AB32
#     PrevPrdSalesRatio_Our: float  # AB34
#     PrevPrdSalesRatio_Other: float  # AB33
#     PrevPrdSales_Sum: float  # V35
#     PrevPrdOperatingProfit: float  # V36
#     PrevPrdOrdinaryIncome: float  # V37
#     LastPrdYear: str  # AE26
#     lastPrdSales_1: float  # AE28
#     lastPrdSales_2: float  # AE29
#     lastPrdSales_3: float  # AE30
#     lastPrdSales_4: float  # AE31
#     lastPrdSales_5: float  # AE32
#     lastPrdSales_Our: float  # AE34
#     lastPrdSales_Other: float  # AE33
#     lastPrdSalesRatio_1: float  # AK28
#     lastPrdSalesRatio_2: float  # AK29
#     lastPrdSalesRatio_3: float  # AK30
#     lastPrdSalesRatio_4: float  # AK31
#     lastPrdSalesRatio_5: float  # AK32
#     lastPrdSalesRatio_Our: float  # AK34
#     lastPrdSalesRatio_Other: float  # AK33
#     lastPrdSales_sum: float  # AE35
#     lastPrdOperatingProfit: float  # AE36
#     lastPrdOrdinaryincome: float  # AE37
#     CurPrdMainProducts: str  # M38
#     MainSupplier_1: str  # W42
#     MainSupplier_2: str  # W43
#     MainSupplier_3: str  # W44
#     MainSupplier_4: str  # W45
#     MainSupplier_5: str  # W46
#     MainSupplierValue_1: float  # AG42
#     MainSupplierValue_2: float  # AG43
#     MainSupplierValue_3: float  # AG44
#     MainSupplierValue_4: float  # AG45
#     MainSupplierValue_5: float  # AG46
#     MainSupplierRatio_1: float  # AK42
#     MainSupplierRatio_2: float  # AK43
#     MainSupplierRatio_3: float  # AK44
#     MainSupplierRatio_4: float  # AK45
#     MainSupplierRatio_5: float  # AK46
#     MainProducts_1: str  # C42
#     MainProducts_2: str  # C43
#     MainProducts_3: str  # C44
#     MainProducts_4: str  # C45
#     MainProducts_5: str  # C46
#
#     def set_cell_data(self, ws):
#         pass
