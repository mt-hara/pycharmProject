from dataclasses import dataclass


@dataclass
class AbstractExcelSheetDTO():
    __xlCustomerCd: str = None  # H3
    __xlCustomerName: str = None  # H5
    __xlCustomerKanaName: str = None  # H4
    __xlHeadOfficeZipCd: str = None  # I7
    __xlHeadOfficeAddress: str = None  # H8
    __xlHeadOfficeTel: str = None  # X7
    __xlHeadOfficeFax: str = None  # AH7
    __xlBranchOfficeZipCd: str = None  # I10
    __xlBranchOfficeAddress: str = None  # H11
    __xlBranchOfficeTel: str = None  # X10
    __xlBranchOfficeFax: str = None  # AH10
    __xlRepName: str = None  # H14
    __xlRepKanaName: str = None  # H13
    __xlRepJobTitle: str = None  # AD13
    __xlRepBirthYear: str = None  # AD14
    __xlRepBirthMonth: str = None  # AH14
    __xlRepBirthDay: str = None  # AK14
    __xlEmployees: int = None  # k22
    __xlEmployeeYear: str = None  # I23
    __xlEmployeeMonth: int = None  # O23
    __xlCapitalForm: int = None  # shape 取得
    __xlCorporateType: str = None  # shape 取得
    __xlCustomerCapital: float = None  # H18
    __xlEstablishedYear: str = None  # O19
    __xlEstablishedMonth: int = None  # I19
    __xlAccountClosingMonth: int = None  # M21
    __xlReturnOnEquity: float = None  # I20
    __xlISO9001Certif: str = None  # D50 shape 取得 取得済 取得予定 取得予定なし
    __xlISO9001Plan: str = None  # D51
    __xlISO9001NoCertif: str = None  # D52
    __xlISO9001ResistedNo: str = None  # N50
    __xlISO9001CertifPlanYear: str = None  # N51
    __xlISO9001CertifPlanMonth: str = None  # R51
    __xlISO14001Certif: str = None  # V50 shape 取得 取得 取得済 取得予定 取得予定なし
    __xlISO14001Plan: str = None  # V51
    __xlISO14001NoCertif: str = None  # V52
    __xlISO14001ResistedNo: str = None  # AF50
    __xlISO14001CertifPlanYear: str = None  # AF51
    __xlISO14001CertifPlanMonth: str = None  # AJ51
    __xlOtherCertif: str = None  # I53
    __xlCustomerBizType: int = None  # shape 取得
    __xlOtherBizType : str = None
    __xlPicName: str = None  # H57
    __xlPicEmailAddress: str = None  # H58
    __xlpicDept: str = None  # H59
    __xlpicPosition: str = None  # G59
    __xlContactZipCd: str = None  # H55
    __xlContactAddress: str = None  # C56
    __xlContactTel: str = None  # H60
    __xlContactFax: str = None  # G60
    __xlStockListingStatus: int = None  # 0:非上場　1:上場 shape 取得
    __xlStockMarket: str = None  # shape 取得 Text
    __xlMainStockholder_1: str = None  # U19
    __xlMainStockholder_2: str = None  # U20
    __xlMainStockholder_3: str = None  # U21
    __xlMainStockholder_4: str = None  # U22
    __xlMainStockholder_5: str = None  # U23
    __xlRatioSH_1: float = None  # AK19
    __xlRatioSH_2: float = None  # AK20
    __xlRatioSH_3: float = None  # AK21
    __xlRatioSH_4: float = None  # AK22
    __xlRatioSH_5: float = None  # AK23
    __xlmainCustomer_1: str = None  # C28
    __xlmainCustomer_2: str = None  # C29
    __xlmainCustomer_3: str = None  # C30
    __xlmainCustomer_4: str = None  # C31
    __xlmainCustomer_5: str = None  # C32
    __xlCurPrdYear: str = None  # M26
    __xlCurPrdSales_1: float = None  # M28
    __xlCurPrdSales_2: float = None  # M29
    __xlCurPrdSales_3: float = None  # M30
    __xlCurPrdSales_4: float = None  # M31
    __xlCurPrdSales_5: float = None  # M32
    __xlCurPrdSales_Our: float = None  # M34
    __xlCurPrdSales_Other: float = None  # M33
    __xlCurPrdSalesRatio_1: float = None  # S28
    __xlCurPrdSalesRatio_2: float = None  # S29
    __xlCurPrdSalesRatio_3: float = None  # S30
    __xlCurPrdSalesRatio_4: float = None  # S31
    __xlCurPrdSalesRatio_5: float = None  # S32
    __xlCurPrdSalesRatio_Our: float = None  # S34
    __xlCurPrdSalesRatio_Othor: float = None  # S33
    __xlCurPrdSales_Sum: float = None  # M35
    __xlCurPrdOperatingProfit: float = None  # M36
    __xlCurPrdOrdinaryincome: float = None  # M37
    __xlPrevPrdYear: str = None  # V26
    __xlPrevPrdSales_1: float = None  # V28
    __xlPrevPrdSales_2: float = None  # V29
    __xlPrevPrdSales_3: float = None  # V30
    __xlPrevPrdSales_4: float = None  # V31
    __xlPrevPrdSales_5: float = None  # V32
    __xlPrevPrdSales_Our: float = None  # V34
    __xlPrevPrdSales_Other: float = None  # V33
    __xlPrevPrdSalesRatio_1: float = None  # AB28
    __xlPrevPrdSalesRatio_2: float = None  # AB29
    __xlPrevPrdSalesRatio_3: float = None  # AB30
    __xlPrevPrdSalesRatio_4: float = None  # AB31
    __xlPrevPrdSalesRatio_5: float = None  # AB32
    __xlPrevPrdSalesRatio_Our: float = None  # AB34
    __xlPrevPrdSalesRatio_Other: float = None  # AB33
    __xlPrevPrdSales_Sum: float = None  # V35
    __xlPrevPrdOperatingProfit: float = None  # V36
    __xlPrevPrdOrdinaryIncome: float = None  # V37
    __xlLastPrdYear: str = None  # AE26
    __xlLastPrdSales_1: float = None  # AE28
    __xlLastPrdSales_2: float = None  # AE29
    __xlLastPrdSales_3: float = None  # AE30
    __xlLastPrdSales_4: float = None  # AE31
    __xlLastPrdSales_5: float = None  # AE32
    __xlLastPrdSales_Our: float = None  # AE34
    __xlLastPrdSales_Other: float = None  # AE33
    __xlLastPrdSalesRatio_1: float = None  # AK28
    __xlLastPrdSalesRatio_2: float = None  # AK29
    __xlLastPrdSalesRatio_3: float = None  # AK30
    __xlLastPrdSalesRatio_4: float = None  # AK31
    __xlLastPrdSalesRatio_5: float = None  # AK32
    __xlLastPrdSalesRatio_Our: float = None  # AK34
    __xlLastPrdSalesRatio_Other: float = None  # AK33
    __xlLastPrdSales_sum: float = None  # AE35
    __xlLastPrdOperatingProfit: float = None  # AE36
    __xlLastPrdOrdinaryIncome: float = None  # AE37
    __xlCurPrdMainProducts: str = None  # M38
    __xlMainSupplier_1: str = None  # W42
    __xlMainSupplier_2: str = None  # W43
    __xlMainSupplier_3: str = None  # W44
    __xlMainSupplier_4: str = None  # W45
    __xlMainSupplier_5: str = None  # W46
    __xlMainSupplierValue_1: float = None  # AG42
    __xlMainSupplierValue_2: float = None  # AG43
    __xlMainSupplierValue_3: float = None  # AG44
    __xlMainSupplierValue_4: float = None  # AG45
    __xlMainSupplierValue_5: float = None  # AG46
    __xlMainSupplierRatio_1: float = None  # AK42
    __xlMainSupplierRatio_2: float = None  # AK43
    __xlMainSupplierRatio_3: float = None  # AK44
    __xlMainSupplierRatio_4: float = None  # AK45
    __xlMainSupplierRatio_5: float = None  # AK46
    __xlMainProducts_1: str = None  # C42
    __xlMainProducts_2: str = None  # C43
    __xlMainProducts_3: str = None  # C44
    __xlMainProducts_4: str = None  # C45
    __xlMainProducts_5: str = None  # C46

    @property
    def xlCustomerCd(self):
        return self.__xlCustomerCd

    @xlCustomerCd.setter
    def xlCustomerCd(self, param: str):
        self.__xlCustomerCd = param

    @property
    def xlCustomerName(self):
        return self.__xlCustomerName

    @xlCustomerName.setter
    def xlCustomerName(self, param: str):
        self.__xlCustomerName = param

    @property
    def xlCustomerKanaName(self):
        return self.__xlCustomerKanaName

    @xlCustomerKanaName.setter
    def xlCustomerKanaName(self, param: str):
        self.__xlCustomerKanaName = param

    @property
    def xlHeadOfficeZipCd(self):
        return self.__xlHeadOfficeZipCd

    @xlHeadOfficeZipCd.setter
    def xlHeadOfficeZipCd(self, param: str):
        self.__xlHeadOfficeZipCd = param

    @property
    def xlHeadOfficeAddress(self):
        return self.__xlHeadOfficeAddress

    @xlHeadOfficeAddress.setter
    def xlHeadOfficeAddress(self, param: str):
        self.__xlHeadOfficeAddress = param

    @property
    def xlHeadOfficeTel(self):
        return self.__xlHeadOfficeTel

    @xlHeadOfficeTel.setter
    def xlHeadOfficeTel(self, param: str):
        self.__xlHeadOfficeTel = param

    @property
    def xlHeadOfficeFax(self):
        return self.__xlHeadOfficeFax

    @xlHeadOfficeFax.setter
    def xlHeadOfficeFax(self, param: str):
        self.__xlHeadOfficeFax = param

    @property
    def xlBranchOfficeZipCd(self):
        return self.__xlBranchOfficeZipCd

    @xlBranchOfficeZipCd.setter
    def xlBranchOfficeZipCd(self, param: str):
        self.__xlBranchOfficeZipCd = param

    @property
    def xlBranchOfficeAddress(self):
        return self.__xlBranchOfficeAddress

    @xlBranchOfficeAddress.setter
    def xlBranchOfficeAddress(self, param: str):
        self.__xlBranchOfficeAddress = param

    @property
    def xlBranchOfficeTel(self):
        return self.__xlBranchOfficeTel

    @xlBranchOfficeTel.setter
    def xlBranchOfficeTel(self, param: str):
        self.__xlBranchOfficeTel = param

    @property
    def xlBranchOfficeFax(self):
        return self.__xlBranchOfficeFax

    @xlBranchOfficeFax.setter
    def xlBranchOfficeFax(self, param: str):
        self.__xlBranchOfficeFax = param

    @property
    def xlRepName(self):
        return self.__xlRepName

    @xlRepName.setter
    def xlRepName(self, param: str):
        self.__xlRepName = param

    @property
    def xlRepKanaName(self):
        return self.__xlRepKanaName

    @xlRepKanaName.setter
    def xlRepKanaName(self, param: str):
        self.__xlRepKanaName = param

    @property
    def xlRepJobTitle(self):
        return self.__xlRepJobTitle

    @xlRepJobTitle.setter
    def xlRepJobTitle(self, param: str):
        self.__xlRepJobTitle = param

    @property
    def xlRepBirthYear(self):
        return self.__xlRepBirthYear

    @xlRepBirthYear.setter
    def xlRepBirthYear(self, param: str):
        self.__xlRepBirthYear = param

    @property
    def xlRepBirthMonth(self):
        return self.__xlRepBirthMonth

    @xlRepBirthMonth.setter
    def xlRepBirthMonth(self, param: str):
        self.__xlRepBirthMonth = param

    @property
    def xlRepBirthDay(self):
        return self.__xlRepBirthDay

    @xlRepBirthDay.setter
    def xlRepBirthDay(self, param: str):
        self.__xlRepBirthDay = param

    @property
    def xlEmployees(self):
        return self.__xlEmployees

    @xlEmployees.setter
    def xlEmployees(self, param: int):
        self.__xlEmployees = param

    @property
    def xlEmployeeYear(self):
        return self.__xlEmployeeYear

    @xlEmployeeYear.setter
    def xlEmployeeYear(self, param: str):
        self.__xlEmployeeYear = param

    @property
    def xlEmployeeMonth(self):
        return self.__xlEmployeeMonth

    @xlEmployeeMonth.setter
    def xlEmployeeMonth(self, param: int):
        self.__xlEmployeeMonth = param

    @property
    def xlCapitalForm(self):
        return self.__xlCapitalForm

    @xlCapitalForm.setter
    def xlCapitalForm(self, param: int):
        self.__xlCapitalForm = param

    @property
    def xlCorporateType(self):
        return self.__xlCorporateType

    @xlCorporateType.setter
    def xlCorporateType(self, param: str):
        self.__xlCorporateType = param

    @property
    def xlCustomerCapital(self):
        return self.__xlCustomerCapital

    @xlCustomerCapital.setter
    def xlCustomerCapital(self, param: float):
        self.__xlCustomerCapital = param

    @property
    def xlEstablishedYear(self):
        return self.__xlEstablishedYear

    @xlEstablishedYear.setter
    def xlEstablishedYear(self, param: str):
        self.__xlEstablishedYear = param

    @property
    def xlEstablishedMonth(self):
        return self.__xlEstablishedMonth

    @xlEstablishedMonth.setter
    def xlEstablishedMonth(self, param: int):
        self.__xlEstablishedMonth = param

    @property
    def xlAccountClosingMonth(self):
        return self.__xlAccountClosingMonth

    @xlAccountClosingMonth.setter
    def xlAccountClosingMonth(self, param: int):
        self.__xlAccountClosingMonth = param

    @property
    def xlReturnOnEquity(self):
        return self.__xlReturnOnEquity

    @xlReturnOnEquity.setter
    def xlReturnOnEquity(self, param: float):
        self.__xlReturnOnEquity = param

    @property
    def xlISO9001Certif(self):
        return self.__xlISO9001Certif

    @xlISO9001Certif.setter
    def xlISO9001Certif(self, param: str):
        self.__xlISO9001Certif = param

    @property
    def xlISO9001Plan(self):
        return self.__xlISO9001Plan

    @xlISO9001Plan.setter
    def xlISO9001Plan(self, param: str):
        self.__xlISO9001Plan = param

    @property
    def xlISO9001NoCertif(self):
        return self.__xlISO9001NoCertif

    @xlISO9001NoCertif.setter
    def xlISO9001NoCertif(self, param: str):
        self.__xlISO9001NoCertif = param

    @property
    def xlISO9001ResistedNo(self):
        return self.__xlISO9001ResistedNo

    @xlISO9001ResistedNo.setter
    def xlISO9001ResistedNo(self, param: str):
        self.__xlISO9001ResistedNo = param

    @property
    def xlISO9001CertifPlanYear(self):
        return self.__xlISO9001CertifPlanYear

    @xlISO9001CertifPlanYear.setter
    def xlISO9001CertifPlanYear(self, param: str):
        self.__xlISO9001CertifPlanYear = param

    @property
    def xlISO9001CertifPlanMonth(self):
        return self.__xlISO9001CertifPlanMonth

    @xlISO9001CertifPlanMonth.setter
    def xlISO9001CertifPlanMonth(self, param: str):
        self.__xlISO9001CertifPlanMonth =param

    @property
    def xlISO14001Certif(self):
        return  self.__xlISO14001Certif

    @xlISO14001Certif.setter
    def xlISO14001Certif(self, param: str):
        self.__xlISO14001Certif = param

    @property
    def xlISO14001Plan(self):
        return self.__xlISO14001Plan

    @xlISO14001Plan.setter
    def xlISO14001Plan(self, param: str):
        self.__xlISO14001Plan = param

    @property
    def xlISO14001NoCertif(self):
        return self.__xlISO14001NoCertif

    @xlISO14001NoCertif.setter
    def xlISO14001NoCertif(self, param: str):
        self.__xlISO14001NoCertif = param

    @property
    def xlISO14001ResistedNo(self):
        return self.__xlISO14001ResistedNo

    @xlISO14001ResistedNo.setter
    def xlISO14001ResistedNo(self, param: str):
        self.__xlISO14001ResistedNo = param

    @property
    def xlISO14001CertifPlanYear(self):
        return self.__xlISO14001CertifPlanYear

    @xlISO14001CertifPlanYear.setter
    def xlISO14001CertifPlanYear(self, param: str):
        self.__xlISO14001CertifPlanYear = param

    @property
    def xlISO14001CertifPlanMonth(self):
        return self.__xlISO14001CertifPlanMonth

    @xlISO14001CertifPlanMonth.setter
    def xlISO14001CertifPlanMonth(self, param: str):
        self.__xlISO14001CertifPlanMonth = param

    @property
    def xlOtherCertif(self):
        return self.__xlOtherCertif

    @xlOtherCertif.setter
    def xlOtherCertif(self, param: str):
        self.__xlOtherCertif = param

    @property
    def xlCustomerBizType(self):
        return self.__xlCustomerBizType

    @xlCustomerBizType.setter
    def xlCustomerBizType(self, param: int):
        self.__xlCustomerBizType = param

    # xlPicName
    # xlPicEmailAddress
    # xlpicDept
    # xlpicPosition
    # xlContactZipCd
    # xlContactAddress
    # xlContactTel
    # xlContactFax
    # xlStockListingStatus
    # xlStockMarket
    # xlMainStockholder_1
    # xlMainStockholder_2
    # xlMainStockholder_3
    # xlMainStockholder_4
    # xlMainStockholder_5
    # xlRatioSH_1
    # xlRatioSH_2
    # xlRatioSH_3
    # xlRatioSH_4
    # xlRatioSH_5
    # xlmainCustomer_1
    # xlmainCustomer_2
    # xlmainCustomer_3
    # xlmainCustomer_4
    # xlmainCustomer_5
    # xlCurPrdYear
    # xlCurPrdSales_1
    # xlCurPrdSales_2
    # xlCurPrdSales_3
    # xlCurPrdSales_4
    # xlCurPrdSales_5
    # xlCurPrdSales_Our
    # xlCurPrdSales_Other
    # xlCurPrdSalesRatio_1
    # xlCurPrdSalesRatio_2
    # xlCurPrdSalesRatio_3
    # xlCurPrdSalesRatio_4
    # xlCurPrdSalesRatio_5
    # xlCurPrdSalesRatio_Our
    # xlCurPrdSalesRatio_Othor
    # xlCurPrdSales_Sum
    # xlCurPrdOperatingProfit
    # xlCurPrdOrdinaryincome
    # xlPrevPrdYear
    # xlPrevPrdSales_1
    # xlPrevPrdSales_2
    # xlPrevPrdSales_3
    # xlPrevPrdSales_4
    # xlPrevPrdSales_5
    # xlPrevPrdSales_Our
    # xlPrevPrdSales_Other
    # xlPrevPrdSalesRatio_1
    # xlPrevPrdSalesRatio_2
    # xlPrevPrdSalesRatio_3
    # xlPrevPrdSalesRatio_4
    # xlPrevPrdSalesRatio_5
    # xlPrevPrdSalesRatio_Our
    # xlPrevPrdSalesRatio_Other
    # xlPrevPrdSales_Sum
    # xlPrevPrdOperatingProfit
    # xlPrevPrdOrdinaryIncome
    # xlLastPrdYear
    # xlLastPrdSales_1
    # xlLastPrdSales_2
    # xlLastPrdSales_3
    # xlLastPrdSales_4
    # xlLastPrdSales_5
    # xlLastPrdSales_Our
    # xlLastPrdSales_Other
    # xlLastPrdSalesRatio_1
    # xlLastPrdSalesRatio_2
    # xlLastPrdSalesRatio_3
    # xlLastPrdSalesRatio_4
    # xlLastPrdSalesRatio_5
    # xlLastPrdSalesRatio_Our
    # xlLastPrdSalesRatio_Other
    # xlLastPrdSales_sum
    # xlLastPrdOperatingProfit
    # xlLastPrdOrdinaryincome
    # xlCurPrdMainProducts
    # xlMainSupplier_1
    # xlMainSupplier_2
    # xlMainSupplier_3
    # xlMainSupplier_4
    # xlMainSupplier_5
    # xlMainSupplierValue_1
    # xlMainSupplierValue_2
    # xlMainSupplierValue_3
    # xlMainSupplierValue_4
    # xlMainSupplierValue_5
    # xlMainSupplierRatio_1
    # xlMainSupplierRatio_2
    # xlMainSupplierRatio_3
    # xlMainSupplierRatio_4
    # xlMainSupplierRatio_5
    # xlMainProducts_1
    # xlMainProducts_2
    # xlMainProducts_3
    # xlMainProducts_4
    # xlMainProducts_5


# @dataclass
# class AbstractExcelSheetDTO():
#     __xlCustomerCd: str = None  # H3
#     __xlCustomerName: str = None  # H5
#     __xlCustomerKanaName: str = None  # H4
#     __xlHeadOfficeZipCd: str = None  # I7
#     __xlHeadOfficeAddress: str = None  # H8
#     __xlHeadOfficeTel: str = None  # X7
#     __xlHeadOfficeFax: str = None  # AH7
#     __xlBranchOfficeZipCd: str = None  # I10
#     __xlBranchOfficeAddress: str = None  # H11
#     __xlBranchOfficeTel: str = None  # X10
#     __xlBranchOfficeFax: str = None  # AH10
#     __xlRepName: str = None  # H14
#     __xlRepKanaName: str = None  # H13
#     __xlRepJobTitle: str = None  # AD13
#     __xlRepBirthYear: str = None  # AD14
#     __xlRepBirthMonth: str = None  # AH14
#     __xlRepBirthDay: str = None  # AK14
#     __xlEmployees: int = None  # k22
#     __xlEmployeeYear: str = None  # I23
#     __xlEmployeeMonth: int = None  # O23
#     __xlCapitalForm: int = None  # shape 取得
#     __xlCorporateType: str = None  # shape 取得
#     __xlCustomerCapital: float = None  # H18
#     __xlEstablishedYear: str = None  # O19
#     __xlEstablishedMonth: int = None  # I19
#     __xlAccountClosingMonth: int = None  # M21
#     __xlReturnOnEquity: float = None  # I20
#     __xlISO9001Certif: str = None  # D50 shape 取得 取得済 取得予定 取得予定なし
#     __xlISO9001Plan: str = None  # D51
#     __xlISO9001NoCertif: str = None  # D52
#     __xlISO9001ResistedNo: str = None  # N50
#     __xlISO9001CertifPlanYear: str = None  # N51
#     __xlISO9001CertifPlanMonth: str = None  # R51
#     __xlISO14001Certif: str = None  # V50 shape 取得 取得 取得済 取得予定 取得予定なし
#     __xlISO14001Plan: str = None  # V51
#     __xlISO14001NoCertif: str = None  # V52
#     __xlISO14001ResistedNo: str = None  # AF50
#     __xlISO14001CertifPlanYear: str = None  # AF51
#     __xlISO14001CertifPlanMonth: str = None  # AJ51
#     __xlOtherCertif: str = None  # I53
#     __xlCustomerBizType: int = None  # shape 取得
#     __xlOtherBizType : str = None
#     __xlPicName: str = None  # H57
#     __xlPicEmailAddress: str = None  # H58
#     __xlpicDept: str = None  # H59
#     __xlpicPosition: str = None  # G59
#     __xlContactZipCd: str = None  # H55
#     __xlContactAddress: str = None  # C56
#     __xlContactTel: str = None  # H60
#     __xlContactFax: str = None  # G60
#     __xlStockListingStatus: int = None  # 0:非上場　1:上場 shape 取得
#     __xlStockMarket: str = None  # shape 取得 Text
#     __xlMainStockholder_1: str = None  # U19
#     __xlMainStockholder_2: str = None  # U20
#     __xlMainStockholder_3: str = None  # U21
#     __xlMainStockholder_4: str = None  # U22
#     __xlMainStockholder_5: str = None  # U23
#     __xlRatioSH_1: float = None  # AK19
#     __xlRatioSH_2: float = None  # AK20
#     __xlRatioSH_3: float = None  # AK21
#     __xlRatioSH_4: float = None  # AK22
#     __xlRatioSH_5: float = None  # AK23
#     __xlmainCustomer_1: str = None  # C28
#     __xlmainCustomer_2: str = None  # C29
#     __xlmainCustomer_3: str = None  # C30
#     __xlmainCustomer_4: str = None  # C31
#     __xlmainCustomer_5: str = None  # C32
#     __xlCurPrdYear: str = None  # M26
#     __xlCurPrdSales_1: float = None  # M28
#     __xlCurPrdSales_2: float = None  # M29
#     __xlCurPrdSales_3: float = None  # M30
#     __xlCurPrdSales_4: float = None  # M31
#     __xlCurPrdSales_5: float = None  # M32
#     __xlCurPrdSales_Our: float = None  # M34
#     __xlCurPrdSales_Other: float = None  # M33
#     __xlCurPrdSalesRatio_1: float = None  # S28
#     __xlCurPrdSalesRatio_2: float = None  # S29
#     __xlCurPrdSalesRatio_3: float = None  # S30
#     __xlCurPrdSalesRatio_4: float = None  # S31
#     __xlCurPrdSalesRatio_5: float = None  # S32
#     __xlCurPrdSalesRatio_Our: float = None  # S34
#     __xlCurPrdSalesRatio_Othor: float = None  # S33
#     __xlCurPrdSales_Sum: float = None  # M35
#     __xlCurPrdOperatingProfit: float = None  # M36
#     __xlCurPrdOrdinaryincome: float = None  # M37
#     __xlPrevPrdYear: str = None  # V26
#     __xlPrevPrdSales_1: float = None  # V28
#     __xlPrevPrdSales_2: float = None  # V29
#     __xlPrevPrdSales_3: float = None  # V30
#     __xlPrevPrdSales_4: float = None  # V31
#     __xlPrevPrdSales_5: float = None  # V32
#     __xlPrevPrdSales_Our: float = None  # V34
#     __xlPrevPrdSales_Other: float = None  # V33
#     __xlPrevPrdSalesRatio_1: float = None  # AB28
#     __xlPrevPrdSalesRatio_2: float = None  # AB29
#     __xlPrevPrdSalesRatio_3: float = None  # AB30
#     __xlPrevPrdSalesRatio_4: float = None  # AB31
#     __xlPrevPrdSalesRatio_5: float = None  # AB32
#     __xlPrevPrdSalesRatio_Our: float = None  # AB34
#     __xlPrevPrdSalesRatio_Other: float = None  # AB33
#     __xlPrevPrdSales_Sum: float = None  # V35
#     __xlPrevPrdOperatingProfit: float = None  # V36
#     __xlPrevPrdOrdinaryIncome: float = None  # V37
#     __xlLastPrdYear: str = None  # AE26
#     __xlLastPrdSales_1: float = None  # AE28
#     __xlLastPrdSales_2: float = None  # AE29
#     __xlLastPrdSales_3: float = None  # AE30
#     __xlLastPrdSales_4: float = None  # AE31
#     __xlLastPrdSales_5: float = None  # AE32
#     __xlLastPrdSales_Our: float = None  # AE34
#     __xlLastPrdSales_Other: float = None  # AE33
#     __xlLastPrdSalesRatio_1: float = None  # AK28
#     __xlLastPrdSalesRatio_2: float = None  # AK29
#     __xlLastPrdSalesRatio_3: float = None  # AK30
#     __xlLastPrdSalesRatio_4: float = None  # AK31
#     __xlLastPrdSalesRatio_5: float = None  # AK32
#     __xlLastPrdSalesRatio_Our: float = None  # AK34
#     __xlLastPrdSalesRatio_Other: float = None  # AK33
#     __xlLastPrdSales_sum: float = None  # AE35
#     __xlLastPrdOperatingProfit: float = None  # AE36
#     __xlLastPrdOrdinaryIncome: float = None  # AE37
#     __xlCurPrdMainProducts: str = None  # M38
#     __xlMainSupplier_1: str = None  # W42
#     __xlMainSupplier_2: str = None  # W43
#     __xlMainSupplier_3: str = None  # W44
#     __xlMainSupplier_4: str = None  # W45
#     __xlMainSupplier_5: str = None  # W46
#     __xlMainSupplierValue_1: float = None  # AG42
#     __xlMainSupplierValue_2: float = None  # AG43
#     __xlMainSupplierValue_3: float = None  # AG44
#     __xlMainSupplierValue_4: float = None  # AG45
#     __xlMainSupplierValue_5: float = None  # AG46
#     __xlMainSupplierRatio_1: float = None  # AK42
#     __xlMainSupplierRatio_2: float = None  # AK43
#     __xlMainSupplierRatio_3: float = None  # AK44
#     __xlMainSupplierRatio_4: float = None  # AK45
#     __xlMainSupplierRatio_5: float = None  # AK46
#     __xlMainProducts_1: str = None  # C42
#     __xlMainProducts_2: str = None  # C43
#     __xlMainProducts_3: str = None  # C44
#     __xlMainProducts_4: str = None  # C45
#     __xlMainProducts_5: str = None  # C46
#
#     @property
#     def xlCustomerCd(self):
#         return self.__xlCustomerCd
#
#     @xlCustomerCd.setter
#     def xlCustomerCd(self, param: str):
#         self.__xlCustomerCd = param
#
#     @property
#     def xlCustomerName(self):
#         return self.__xlCustomerName
#
#     @xlCustomerName.setter
#     def xlCustomerName(self, param: str):
#         self.__xlCustomerName = param
#
#     @property
#     def xlCustomerKanaName(self):
#         return self.__xlCustomerKanaName
#
#     @xlCustomerKanaName.setter
#     def xlCustomerKanaName(self, param: str):
#         self.__xlCustomerKanaName = param
#
#     @property
#     def xlHeadOfficeZipCd(self):
#         return self.__xlHeadOfficeZipCd
#
#     @xlHeadOfficeZipCd.setter
#     def xlHeadOfficeZipCd(self, param: str):
#         self.__xlHeadOfficeZipCd = param
#
#     @property
#     def xlHeadOfficeAddress(self):
#         return self.__xlHeadOfficeAddress
#
#     @xlHeadOfficeAddress.setter
#     def xlHeadOfficeAddress(self, param: str):
#         self.__xlHeadOfficeAddress = param
#
#     @property
#     def xlHeadOfficeTel(self):
#         return self.__xlHeadOfficeTel
#
#     @xlHeadOfficeTel.setter
#     def xlHeadOfficeTel(self, param: str):
#         self.__xlHeadOfficeTel = param
#
#     @property
#     def xlHeadOfficeFax(self):
#         return self.__xlHeadOfficeFax
#
#     @xlHeadOfficeFax.setter
#     def xlHeadOfficeFax(self, param: str):
#         self.__xlHeadOfficeFax = param
#
#     @property
#     def xlBranchOfficeZipCd(self):
#         return self.__xlBranchOfficeZipCd
#
#     @xlBranchOfficeZipCd.setter
#     def xlBranchOfficeZipCd(self, param: str):
#         self.__xlBranchOfficeZipCd = param
#
#     @property
#     def xlBranchOfficeAddress(self):
#         return self.__xlBranchOfficeAddress
#
#     @xlBranchOfficeAddress.setter
#     def xlBranchOfficeAddress(self, param: str):
#         self.__xlBranchOfficeAddress = param
#
#     @property
#     def xlBranchOfficeTel(self):
#         return self.__xlBranchOfficeTel
#
#     @xlBranchOfficeTel.setter
#     def xlBranchOfficeTel(self, param: str):
#         self.__xlBranchOfficeTel = param
#
#     @property
#     def xlBranchOfficeFax(self):
#         return self.__xlBranchOfficeFax
#
#     @xlBranchOfficeFax.setter
#     def xlBranchOfficeFax(self, param: str):
#         self.__xlBranchOfficeFax = param
#
#     @property
#     def xlRepName(self):
#         return self.__xlRepName
#
#     @xlRepName.setter
#     def xlRepName(self, param: str):
#         self.__xlRepName = param
#
#     @property
#     def xlRepKanaName(self):
#         return self.__xlRepKanaName
#
#     @xlRepKanaName.setter
#     def xlRepKanaName(self, param: str):
#         self.__xlRepKanaName = param
#
#     @property
#     def xlRepJobTitle(self):
#         return self.__xlRepJobTitle
#
#     @xlRepJobTitle.setter
#     def xlRepJobTitle(self, param: str):
#         self.__xlRepJobTitle = param
#
#     @property
#     def xlRepBirthYear(self):
#         return self.__xlRepBirthYear
#
#     @xlRepBirthYear.setter
#     def xlRepBirthYear(self, param: str):
#         self.__xlRepBirthYear = param
#
#     @property
#     def xlRepBirthMonth(self):
#         return self.__xlRepBirthMonth
#
#     @xlRepBirthMonth.setter
#     def xlRepBirthMonth(self, param: str):
#         self.__xlRepBirthMonth = param
#
#     @property
#     def xlRepBirthDay(self):
#         return self.__xlRepBirthDay
#
#     @xlRepBirthDay.setter
#     def xlRepBirthDay(self, param: str):
#         self.__xlRepBirthDay = param
#
#     @property
#     def xlEmployees(self):
#         return self.__xlEmployees
#
#     @xlEmployees.setter
#     def xlEmployees(self, param: int):
#         self.__xlEmployees = param
#
#     @property
#     def xlEmployeeYear(self):
#         return self.__xlEmployeeYear
#
#     @xlEmployeeYear.setter
#     def xlEmployeeYear(self, param: str):
#         self.__xlEmployeeYear = param
#
#     @property
#     def xlEmployeeMonth(self):
#         return self.__xlEmployeeMonth
#
#     @xlEmployeeMonth.setter
#     def xlEmployeeMonth(self, param: int):
#         self.__xlEmployeeMonth = param
#
#     @property
#     def xlCapitalForm(self):
#         return self.__xlCapitalForm
#
#     @xlCapitalForm.setter
#     def xlCapitalForm(self, param: int):
#         self.__xlCapitalForm = param
#
#     @property
#     def xlCorporateType(self):
#         return self.__xlCorporateType
#
#     @xlCorporateType.setter
#     def xlCorporateType(self, param: str):
#         self.__xlCorporateType = param
#
#     @property
#     def xlCustomerCapital(self):
#         return self.__xlCustomerCapital
#
#     @xlCustomerCapital.setter
#     def xlCustomerCapital(self, param: float):
#         self.__xlCustomerCapital = param
#
#     @property
#     def xlEstablishedYear(self):
#         return self.__xlEstablishedYear
#
#     @xlEstablishedYear.setter
#     def xlEstablishedYear(self, param: str):
#         self.__xlEstablishedYear = param
#
#     @property
#     def xlEstablishedMonth(self):
#         return self.__xlEstablishedMonth
#
#     @xlEstablishedMonth.setter
#     def xlEstablishedMonth(self, param: int):
#         self.__xlEstablishedMonth = param
#
#     @property
#     def xlAccountClosingMonth(self):
#         return self.__xlAccountClosingMonth
#
#     @xlAccountClosingMonth.setter
#     def xlAccountClosingMonth(self, param: int):
#         self.__xlAccountClosingMonth = param
#
#     @property
#     def xlReturnOnEquity(self):
#         return self.__xlReturnOnEquity
#
#     @xlReturnOnEquity.setter
#     def xlReturnOnEquity(self, param: float):
#         self.__xlReturnOnEquity = param
#
#     @property
#     def xlISO9001Certif(self):
#         return self.__xlISO9001Certif
#
#     @xlISO9001Certif.setter
#     def xlISO9001Certif(self, param: str):
#         self.__xlISO9001Certif = param
#
#     @property
#     def xlISO9001Plan(self):
#         return self.__xlISO9001Plan
#
#     @xlISO9001Plan.setter
#     def xlISO9001Plan(self, param: str):
#         self.__xlISO9001Plan = param
#
#     @property
#     def xlISO9001NoCertif(self):
#         return self.__xlISO9001NoCertif
#
#     @xlISO9001NoCertif.setter
#     def xlISO9001NoCertif(self, param: str):
#         self.__xlISO9001NoCertif = param
#
#     @property
#     def xlISO9001ResistedNo(self):
#         return self.__xlISO9001ResistedNo
#
#     @xlISO9001ResistedNo.setter
#     def xlISO9001ResistedNo(self, param: str):
#         self.__xlISO9001ResistedNo = param
#
#     @property
#     def xlISO9001CertifPlanYear(self):
#         return self.__xlISO9001CertifPlanYear
#
#     @xlISO9001CertifPlanYear.setter
#     def xlISO9001CertifPlanYear(self, param: str):
#         self.__xlISO9001CertifPlanYear = param
#
#     @property
#     def xlISO9001CertifPlanMonth(self):
#         return self.__xlISO9001CertifPlanMonth
#
#     @xlISO9001CertifPlanMonth.setter
#     def xlISO9001CertifPlanMonth(self, param: str):
#         self.__xlISO9001CertifPlanMonth =param
#
#     @property
#     def xlISO14001Certif(self):
#         return  self.__xlISO14001Certif
#
#     @xlISO14001Certif.setter
#     def xlISO14001Certif(self, param: str):
#         self.__xlISO14001Certif = param
#
#     @property
#     def xlISO14001Plan(self):
#         return self.__xlISO14001Plan
#
#     @xlISO14001Plan.setter
#     def xlISO14001Plan(self, param: str):
#         self.__xlISO14001Plan = param
#
#     @property
#     def xlISO14001NoCertif(self):
#         return self.__xlISO14001NoCertif
#
#     @xlISO14001NoCertif.setter
#     def xlISO14001NoCertif(self, param: str):
#         self.__xlISO14001NoCertif = param
#
#     @property
#     def xlISO14001ResistedNo(self):
#         return self.__xlISO14001ResistedNo
#
#     @xlISO14001ResistedNo.setter
#     def xlISO14001ResistedNo(self, param: str):
#         self.__xlISO14001ResistedNo = param
#
#     @property
#     def xlISO14001CertifPlanYear(self):
#         return self.__xlISO14001CertifPlanYear
#
#     @xlISO14001CertifPlanYear.setter
#     def xlISO14001CertifPlanYear(self, param: str):
#         self.__xlISO14001CertifPlanYear = param
#
#     @property
#     def xlISO14001CertifPlanMonth(self):
#         return self.__xlISO14001CertifPlanMonth
#
#     @xlISO14001CertifPlanMonth.setter
#     def xlISO14001CertifPlanMonth(self, param: str):
#         self.__xlISO14001CertifPlanMonth = param
#
#     @property
#     def xlOtherCertif(self):
#         return self.__xlOtherCertif
#
#     @xlOtherCertif.setter
#     def xlOtherCertif(self, param: str):
#         self.__xlOtherCertif = param
#
#     @property
#     def xlCustomerBizType(self):
#         return self.__xlCustomerBizType
#
#     @xlCustomerBizType.setter
#     def xlCustomerBizType(self, param: int):
#         self.__xlCustomerBizType = param



    # xlPicName
    # xlPicEmailAddress
    # xlpicDept
    # xlpicPosition
    # xlContactZipCd
    # xlContactAddress
    # xlContactTel
    # xlContactFax
    # xlStockListingStatus
    # xlStockMarket
    # xlMainStockholder_1
    # xlMainStockholder_2
    # xlMainStockholder_3
    # xlMainStockholder_4
    # xlMainStockholder_5
    # xlRatioSH_1
    # xlRatioSH_2
    # xlRatioSH_3
    # xlRatioSH_4
    # xlRatioSH_5
    # xlmainCustomer_1
    # xlmainCustomer_2
    # xlmainCustomer_3
    # xlmainCustomer_4
    # xlmainCustomer_5
    # xlCurPrdYear
    # xlCurPrdSales_1
    # xlCurPrdSales_2
    # xlCurPrdSales_3
    # xlCurPrdSales_4
    # xlCurPrdSales_5
    # xlCurPrdSales_Our
    # xlCurPrdSales_Other
    # xlCurPrdSalesRatio_1
    # xlCurPrdSalesRatio_2
    # xlCurPrdSalesRatio_3
    # xlCurPrdSalesRatio_4
    # xlCurPrdSalesRatio_5
    # xlCurPrdSalesRatio_Our
    # xlCurPrdSalesRatio_Othor
    # xlCurPrdSales_Sum
    # xlCurPrdOperatingProfit
    # xlCurPrdOrdinaryincome
    # xlPrevPrdYear
    # xlPrevPrdSales_1
    # xlPrevPrdSales_2
    # xlPrevPrdSales_3
    # xlPrevPrdSales_4
    # xlPrevPrdSales_5
    # xlPrevPrdSales_Our
    # xlPrevPrdSales_Other
    # xlPrevPrdSalesRatio_1
    # xlPrevPrdSalesRatio_2
    # xlPrevPrdSalesRatio_3
    # xlPrevPrdSalesRatio_4
    # xlPrevPrdSalesRatio_5
    # xlPrevPrdSalesRatio_Our
    # xlPrevPrdSalesRatio_Other
    # xlPrevPrdSales_Sum
    # xlPrevPrdOperatingProfit
    # xlPrevPrdOrdinaryIncome
    # xlLastPrdYear
    # xlLastPrdSales_1
    # xlLastPrdSales_2
    # xlLastPrdSales_3
    # xlLastPrdSales_4
    # xlLastPrdSales_5
    # xlLastPrdSales_Our
    # xlLastPrdSales_Other
    # xlLastPrdSalesRatio_1
    # xlLastPrdSalesRatio_2
    # xlLastPrdSalesRatio_3
    # xlLastPrdSalesRatio_4
    # xlLastPrdSalesRatio_5
    # xlLastPrdSalesRatio_Our
    # xlLastPrdSalesRatio_Other
    # xlLastPrdSales_sum
    # xlLastPrdOperatingProfit
    # xlLastPrdOrdinaryincome
    # xlCurPrdMainProducts
    # xlMainSupplier_1
    # xlMainSupplier_2
    # xlMainSupplier_3
    # xlMainSupplier_4
    # xlMainSupplier_5
    # xlMainSupplierValue_1
    # xlMainSupplierValue_2
    # xlMainSupplierValue_3
    # xlMainSupplierValue_4
    # xlMainSupplierValue_5
    # xlMainSupplierRatio_1
    # xlMainSupplierRatio_2
    # xlMainSupplierRatio_3
    # xlMainSupplierRatio_4
    # xlMainSupplierRatio_5
    # xlMainProducts_1
    # xlMainProducts_2
    # xlMainProducts_3
    # xlMainProducts_4
    # xlMainProducts_5
