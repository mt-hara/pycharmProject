class AbstractExcelSheetDTO():
    def __init__(self):
        self.__xlCustomerCd: str = ""  # H3
        self.__xlCustomerName: str = ""  # H5
        self.__xlCustomerKanaName: str = ""  # H4
        self.__xlHeadOfficeZipCd: str = ""  # I7
        self.__xlHeadOfficeAddress: str = ""  # H8
        self.__xlHeadOfficeTel: str = ""  # X7
        self.__xlHeadOfficeFax: str = ""  # AH7
        self.__xlBranchOfficeZipCd: str = ""  # I10
        self.__xlBranchOfficeAddress: str = ""  # H11
        self.__xlBranchOfficeTel: str = ""  # X10
        self.__xlBranchOfficeFax: str = ""  # AH10
        self.__xlRepName: str = ""  # H14
        self.__xlRepKanaName: str = ""  # H13
        self.__xlRepJobTitle: str = ""  # AD13
        self.__xlRepBirthYear: str = ""  # AD14
        self.__xlRepBirthMonth: str = ""  # AH14
        self.__xlRepBirthDay: str = ""  # AK14
        self.__xlEmployees: int = 0  # k22
        self.__xlEmployeeYear: str = ""  # I23
        self.__xlEmployeeMonth: str = ""  # O23
        self.__xlCapitalForm: str = ""  # shape 取得
        self.__xlCorporateType: str = ""  # shape 取得
        self.__xlCustomerCapital: float = 0  # H18
        self.__xlEstablishedYear: str = ""  # O19
        self.__xlEstablishedMonth: str = ""  # I19
        self.__xlAccountClosingMonth: int = 0  # M21
        self.__xlReturnOnEquity: float = 0  # I20
        self.__xlISO9001Certif: str = ""  # D50 shape 取得 取得済 取得予定 取得予定なし
        self.__xlISO9001Plan: str = ""  # D51
        self.__xlISO9001NoCertif: str = ""  # D52
        self.__xlISO9001ResistedNo: str = ""  # N50
        self.__xlISO9001CertifPlanYear: str = ""  # N51
        self.__xlISO9001CertifPlanMonth: str = ""  # R51
        self.__xlISO14001Certif: str = ""  # V50 shape 取得 取得 取得済 取得予定 取得予定なし
        self.__xlISO14001Plan: str = ""  # V51
        self.__xlISO14001NoCertif: str = ""  # V52
        self.__xlISO14001ResistedNo: str = ""  # AF50
        self.__xlISO14001CertifPlanYear: str = ""  # AF51
        self.__xlISO14001CertifPlanMonth: str = ""  # AJ51
        self.__xlOtherCertif: str = ""  # I53
        self.__xlCustomerBizType: str = ""  # shape 取得
        self.__xlOtherBizType: str = ""  # 手入力
        self.__xlPicName: str = ""  # H57
        self.__xlPicEmailAddress: str = ""  # H58
        self.__xlPicDept: str = ""  # H59
        self.__xlPicPosition: str = ""  # G59
        self.__xlContactZipCd: str = ""  # H55
        self.__xlContactAddress: str = ""  # C56
        self.__xlContactTel: str = ""  # H60
        self.__xlContactFax: str = ""  # G60
        self.__xlStockListingStatus: str = ""  # 0:非上場　1:上場 shape 取得
        self.__xlStockMarket: str = ""  # shape 取得 Text
        self.__xlMainStockholder_1: str = ""  # U19
        self.__xlMainStockholder_2: str = ""  # U20
        self.__xlMainStockholder_3: str = ""  # U21
        self.__xlMainStockholder_4: str = ""  # U22
        self.__xlMainStockholder_5: str = ""  # U23
        self.__xlRatioSH_1: float = 0  # AK19
        self.__xlRatioSH_2: float = 0  # AK20
        self.__xlRatioSH_3: float = 0  # AK21
        self.__xlRatioSH_4: float = 0  # AK22
        self.__xlRatioSH_5: float = 0  # AK23
        self.__xlmainCustomer_1: str = ""  # C28
        self.__xlmainCustomer_2: str = ""  # C29
        self.__xlmainCustomer_3: str = ""  # C30
        self.__xlmainCustomer_4: str = ""  # C31
        self.__xlmainCustomer_5: str = ""  # C32
        self.__xlCurPrdYear: str = ""  # M26
        self.__xlCurPrdSales_1: int = 0  # M28
        self.__xlCurPrdSales_2: int = 0  # M29
        self.__xlCurPrdSales_3: int = 0  # M30
        self.__xlCurPrdSales_4: int = 0  # M31
        self.__xlCurPrdSales_5: int = 0  # M32
        self.__xlCurPrdSales_Our: int = 0  # M34
        self.__xlCurPrdSales_Other: int = 0  # M33
        self.__xlCurPrdSalesRatio_1: float = 0  # S28
        self.__xlCurPrdSalesRatio_2: float = 0  # S29
        self.__xlCurPrdSalesRatio_3: float = 0  # S30
        self.__xlCurPrdSalesRatio_4: float = 0  # S31
        self.__xlCurPrdSalesRatio_5: float = 0  # S32
        self.__xlCurPrdSalesRatio_Our: float = 0  # S34
        self.__xlCurPrdSalesRatio_Othor: float = 0  # S33
        self.__xlCurPrdSales_Sum: int = 0  # M35
        self.__xlCurPrdOperatingProfit: int = 0  # M36
        self.__xlCurPrdOrdinaryIncome: int = 0  # M37
        self.__xlPrevPrdYear: str = ""  # V26
        self.__xlPrevPrdSales_1: int = 0  # V28
        self.__xlPrevPrdSales_2: int = 0  # V29
        self.__xlPrevPrdSales_3: int = 0  # V30
        self.__xlPrevPrdSales_4: int = 0  # V31
        self.__xlPrevPrdSales_5: int = 0  # V32
        self.__xlPrevPrdSales_Our: int = 0  # V34
        self.__xlPrevPrdSales_Other: int = 0  # V33
        self.__xlPrevPrdSalesRatio_1: float = 0  # AB28
        self.__xlPrevPrdSalesRatio_2: float = 0  # AB29
        self.__xlPrevPrdSalesRatio_3: float = 0  # AB30
        self.__xlPrevPrdSalesRatio_4: float = 0  # AB31
        self.__xlPrevPrdSalesRatio_5: float = 0  # AB32
        self.__xlPrevPrdSalesRatio_Our: float = 0  # AB34
        self.__xlPrevPrdSalesRatio_Other: float = 0  # AB33
        self.__xlPrevPrdSales_Sum: int = 0  # V35
        self.__xlPrevPrdOperatingProfit: int = 0  # V36
        self.__xlPrevPrdOrdinaryIncome: int = 0  # V37
        self.__xlLastPrdYear: str = ""  # AE26
        self.__xlLastPrdSales_1: int = 0  # AE28
        self.__xlLastPrdSales_2: int = 0  # AE29
        self.__xlLastPrdSales_3: int = 0  # AE30
        self.__xlLastPrdSales_4: int = 0  # AE31
        self.__xlLastPrdSales_5: int = 0  # AE32
        self.__xlLastPrdSales_Our: int = 0  # AE34
        self.__xlLastPrdSales_Other: int = 0  # AE33
        self.__xlLastPrdSalesRatio_1: float = 0  # AK28
        self.__xlLastPrdSalesRatio_2: float = 0  # AK29
        self.__xlLastPrdSalesRatio_3: float = 0  # AK30
        self.__xlLastPrdSalesRatio_4: float = 0  # AK31
        self.__xlLastPrdSalesRatio_5: float = 0  # AK32
        self.__xlLastPrdSalesRatio_Our: float = 0  # AK34
        self.__xlLastPrdSalesRatio_Other: float = 0  # AK33
        self.__xlLastPrdSales_Sum: int = 0  # AE35
        self.__xlLastPrdOperatingProfit: int = 0  # AE36
        self.__xlLastPrdOrdinaryIncome: int = 0  # AE37
        self.__xlCurPrdMainProducts: str = ""  # M38
        self.__xlMainSupplier_1: str = ""  # W42
        self.__xlMainSupplier_2: str = ""  # W43
        self.__xlMainSupplier_3: str = ""  # W44
        self.__xlMainSupplier_4: str = ""  # W45
        self.__xlMainSupplier_5: str = ""  # W46
        self.__xlMainSupplierValue_1: int = 0  # AG42
        self.__xlMainSupplierValue_2: int = 0  # AG43
        self.__xlMainSupplierValue_3: int = 0  # AG44
        self.__xlMainSupplierValue_4: int = 0  # AG45
        self.__xlMainSupplierValue_5: int = 0  # AG46
        self.__xlMainSupplierRatio_1: float = 0  # AK42
        self.__xlMainSupplierRatio_2: float = 0  # AK43
        self.__xlMainSupplierRatio_3: float = 0  # AK44
        self.__xlMainSupplierRatio_4: float = 0  # AK45
        self.__xlMainSupplierRatio_5: float = 0  # AK46
        self.__xlMainProducts_1: str = ""  # C42
        self.__xlMainProducts_2: str = ""  # C43
        self.__xlMainProducts_3: str = ""  # C44
        self.__xlMainProducts_4: str = ""  # C45
        self.__xlMainProducts_5: str = ""  # C46

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
    def xlEmployeeMonth(self, param: str):
        self.__xlEmployeeMonth = param

    @property
    def xlCapitalForm(self):
        return self.__xlCapitalForm

    @xlCapitalForm.setter
    def xlCapitalForm(self, param: str):
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
    def xlEstablishedMonth(self, param: str):
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
        self.__xlISO9001CertifPlanMonth = param

    @property
    def xlISO14001Certif(self):
        return self.__xlISO14001Certif

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
    def xlCustomerBizType(self, param: str):
        self.__xlCustomerBizType = param

    @property
    def xlOtherBizType(self):
        return self.__xlOtherBizType

    @xlOtherBizType.setter
    def xlOtherBizType(self, param: str):
        self.__xlOtherBizType = param

    @property
    def xlPicName(self):
        return self.__xlPicName

    @xlPicName.setter
    def xlPicName(self, param: str):
        self.__xlPicName = param

    @property
    def xlPicEmailAddress(self):
        return self.__xlPicEmailAddress

    @xlPicEmailAddress.setter
    def xlPicEmailAddress(self, param: str):
        self.__xlPicEmailAddress = param

    @property
    def xlPicDept(self):
        return self.__xlPicDept

    @xlPicDept.setter
    def xlPicDept(self, param: str):
        self.__xlPicDept = param

    @property
    def xlPicPosition(self):
        return self.__xlPicPosition

    @xlPicPosition.setter
    def xlPicPosition(self, param: str):
        self.__xlPicPosition = param

    @property
    def xlContactZipCd(self):
        return self.__xlContactZipCd

    @xlContactZipCd.setter
    def xlContactZipCd(self, param: str):
        self.__xlContactZipCd = param

    @property
    def xlContactAddress(self):
        return self.__xlContactAddress

    @xlContactAddress.setter
    def xlContactAddress(self, param: str):
        self.__xlContactAddress = param

    @property
    def xlContactTel(self):
        return self.__xlContactTel

    @xlContactTel.setter
    def xlContactTel(self, param: str):
        self.__xlContactTel = param

    @property
    def xlContactFax(self):
        return self.__xlContactFax

    @xlContactFax.setter
    def xlContactFax(self, param: str):
        self.__xlContactFax = param

    @property
    def xlStockListingStatus(self):
        return self.__xlStockListingStatus

    @xlStockListingStatus.setter
    def xlStockListingStatus(self, param: str):
        self.__xlStockListingStatus = param

    @property
    def xlStockMarket(self):
        return self.__xlStockMarket

    @xlStockMarket.setter
    def xlStockMarket(self, param: str):
        self.__xlStockMarket = param

    @property
    def xlMainStockholder_1(self):
        return self.__xlMainStockholder_1

    @xlMainStockholder_1.setter
    def xlMainStockholder_1(self, param: str):
        self.__xlMainStockholder_1 = param

    @property
    def xlMainStockholder_2(self):
        return self.__xlMainStockholder_2

    @xlMainStockholder_2.setter
    def xlMainStockholder_2(self, param: str):
        self.__xlMainStockholder_2 = param

    @property
    def xlMainStockholder_3(self):
        return self.__xlMainStockholder_3

    @xlMainStockholder_3.setter
    def xlMainStockholder_3(self, param: str):
        self.__xlMainStockholder_3 = param

    @property
    def xlMainStockholder_4(self):
        return self.__xlMainStockholder_4

    @xlMainStockholder_4.setter
    def xlMainStockholder_4(self, param: str):
        self.__xlMainStockholder_4 = param

    @property
    def xlMainStockholder_5(self):
        return self.__xlMainStockholder_5

    @xlMainStockholder_5.setter
    def xlMainStockholder_5(self, param: str):
        self.__xlMainStockholder_5 = param

    @property
    def xlRatioSH_1(self):
        return self.__xlRatioSH_1

    @xlRatioSH_1.setter
    def xlRatioSH_1(self, param: float):
        self.__xlRatioSH_1 = param

    @property
    def xlRatioSH_2(self):
        return self.__xlRatioSH_2

    @xlRatioSH_2.setter
    def xlRatioSH_2(self, param: float):
        self.__xlRatioSH_2 = param

    @property
    def xlRatioSH_3(self):
        return self.__xlRatioSH_3

    @xlRatioSH_3.setter
    def xlRatioSH_3(self, param: float):
        self.__xlRatioSH_3 = param

    @property
    def xlRatioSH_4(self):
        return self.__xlRatioSH_4

    @xlRatioSH_4.setter
    def xlRatioSH_4(self, param: float):
        self.__xlRatioSH_4 = param

    @property
    def xlRatioSH_5(self):
        return self.__xlRatioSH_5

    @xlRatioSH_5.setter
    def xlRatioSH_5(self, param: float):
        self.__xlRatioSH_5 = param

    @property
    def xlmainCustomer_1(self):
        return self.__xlmainCustomer_1

    @xlmainCustomer_1.setter
    def xlmainCustomer_1(self, param: str):
        self.__xlmainCustomer_1 = param

    @property
    def xlmainCustomer_2(self):
        return self.__xlmainCustomer_2

    @xlmainCustomer_2.setter
    def xlmainCustomer_2(self, param: str):
        self.__xlmainCustomer_2 = param

    @property
    def xlmainCustomer_3(self):
        return self.__xlmainCustomer_3

    @xlmainCustomer_3.setter
    def xlmainCustomer_3(self, param: str):
        self.__xlmainCustomer_3 = param

    @property
    def xlmainCustomer_4(self):
        return self.__xlmainCustomer_4

    @xlmainCustomer_4.setter
    def xlmainCustomer_4(self, param: str):
        self.__xlmainCustomer_4 = param

    @property
    def xlmainCustomer_5(self):
        return self.__xlmainCustomer_5

    @xlmainCustomer_5.setter
    def xlmainCustomer_5(self, param: str):
        self.__xlmainCustomer_5 = param

    @property
    def xlCurPrdYear(self):
        return self.__xlCurPrdYear

    @xlCurPrdYear.setter
    def xlCurPrdYear(self, param: str):
        self.__xlCurPrdYear = param

    @property
    def xlCurPrdSales_1(self):
        return self.__xlCurPrdSales_1

    @xlCurPrdSales_1.setter
    def xlCurPrdSales_1(self, param: float):
        self.__xlCurPrdSales_1 = param

    @property
    def xlCurPrdSales_2(self):
        return self.__xlCurPrdSales_2

    @xlCurPrdSales_2.setter
    def xlCurPrdSales_2(self, param: float):
        self.__xlCurPrdSales_2 = param

    @property
    def xlCurPrdSales_3(self):
        return self.__xlCurPrdSales_3

    @xlCurPrdSales_3.setter
    def xlCurPrdSales_3(self, param: float):
        self.__xlCurPrdSales_3 = param

    @property
    def xlCurPrdSales_4(self):
        return self.__xlCurPrdSales_4

    @xlCurPrdSales_4.setter
    def xlCurPrdSales_4(self, param: float):
        self.__xlCurPrdSales_4 = param

    @property
    def xlCurPrdSales_5(self):
        return self.__xlCurPrdSales_5

    @xlCurPrdSales_5.setter
    def xlCurPrdSales_5(self, param: float):
        self.__xlCurPrdSales_5 = param

    @property
    def xlCurPrdSales_Our(self):
        return self.__xlCurPrdSales_Our

    @xlCurPrdSales_Our.setter
    def xlCurPrdSales_Our(self, param: float):
        self.__xlCurPrdSales_Our = param

    @property
    def xlCurPrdSales_Other(self):
        return self.__xlCurPrdSales_Other

    @xlCurPrdSales_Other.setter
    def xlCurPrdSales_Other(self, param: float):
        self.__xlCurPrdSales_Other = param

    @property
    def xlCurPrdSalesRatio_1(self):
        return self.__xlCurPrdSalesRatio_1

    @xlCurPrdSalesRatio_1.setter
    def xlCurPrdSalesRatio_1(self, param: float):
        self.__xlCurPrdSalesRatio_1 = param

    @property
    def xlCurPrdSalesRatio_2(self):
        return self.__xlCurPrdSalesRatio_2

    @xlCurPrdSalesRatio_2.setter
    def xlCurPrdSalesRatio_2(self, param: float):
        self.__xlCurPrdSalesRatio_2 = param

    @property
    def xlCurPrdSalesRatio_3(self):
        return self.__xlCurPrdSalesRatio_3

    @xlCurPrdSalesRatio_3.setter
    def xlCurPrdSalesRatio_3(self, param: float):
        self.__xlCurPrdSalesRatio_3 = param

    @property
    def xlCurPrdSalesRatio_4(self):
        return self.__xlCurPrdSalesRatio_4

    @xlCurPrdSalesRatio_4.setter
    def xlCurPrdSalesRatio_4(self, param: float):
        self.__xlCurPrdSalesRatio_4 = param

    @property
    def xlCurPrdSalesRatio_5(self):
        return self.__xlCurPrdSalesRatio_5

    @xlCurPrdSalesRatio_5.setter
    def xlCurPrdSalesRatio_5(self, param: float):
        self.__xlCurPrdSalesRatio_5 = param

    @property
    def xlCurPrdSalesRatio_Our(self):
        return self.__xlCurPrdSalesRatio_Our

    @xlCurPrdSalesRatio_Our.setter
    def xlCurPrdSalesRatio_Our(self, param: float):
        self.__xlCurPrdSalesRatio_Our = param

    @property
    def xlCurPrdSalesRatio_Othor(self):
        return self.__xlCurPrdSalesRatio_Othor

    @xlCurPrdSalesRatio_Othor.setter
    def xlCurPrdSalesRatio_Othor(self, param: float):
        self.__xlCurPrdSalesRatio_Othor = param

    @property
    def xlCurPrdSales_Sum(self):
        return self.__xlCurPrdSales_Sum

    @xlCurPrdSales_Sum.setter
    def xlCurPrdSales_Sum(self, param: float):
        self.__xlCurPrdSales_Sum = param

    @property
    def xlCurPrdOperatingProfit(self):
        return self.__xlCurPrdOperatingProfit

    @xlCurPrdOperatingProfit.setter
    def xlCurPrdOperatingProfit(self, param: float):
        self.__xlCurPrdOperatingProfit = param

    @property
    def xlCurPrdOrdinaryIncome(self):
        return self.__xlCurPrdOrdinaryIncome

    @xlCurPrdOrdinaryIncome.setter
    def xlCurPrdOrdinaryIncome(self, param: float):
        self.__xlCurPrdOrdinaryIncome = param

    @property
    def xlPrevPrdYear(self):
        return self.__xlPrevPrdYear

    @xlPrevPrdYear.setter
    def xlPrevPrdYear(self, param: str):
        self.__xlPrevPrdYear = param

    @property
    def xlPrevPrdSales_1(self):
        return self.__xlPrevPrdSales_1

    @xlPrevPrdSales_1.setter
    def xlPrevPrdSales_1(self, param: float):
        self.__xlPrevPrdSales_1 = param

    @property
    def xlPrevPrdSales_2(self):
        return self.__xlPrevPrdSales_2

    @xlPrevPrdSales_2.setter
    def xlPrevPrdSales_2(self, param: float):
        self.__xlPrevPrdSales_2 = param

    @property
    def xlPrevPrdSales_3(self):
        return self.__xlPrevPrdSales_3

    @xlPrevPrdSales_3.setter
    def xlPrevPrdSales_3(self, param: float):
        self.__xlPrevPrdSales_3 = param

    @property
    def xlPrevPrdSales_4(self):
        return self.__xlPrevPrdSales_4

    @xlPrevPrdSales_4.setter
    def xlPrevPrdSales_4(self, param: float):
        self.__xlPrevPrdSales_4 = param

    @property
    def xlPrevPrdSales_5(self):
        return self.__xlPrevPrdSales_5

    @xlPrevPrdSales_5.setter
    def xlPrevPrdSales_5(self, param: float):
        self.__xlPrevPrdSales_5 = param

    @property
    def xlPrevPrdSales_Our(self):
        return self.__xlPrevPrdSales_Our

    @xlPrevPrdSales_Our.setter
    def xlPrevPrdSales_Our(self, param: float):
        self.__xlPrevPrdSales_Our = param

    @property
    def xlPrevPrdSales_Other(self):
        return self.__xlPrevPrdSales_Other

    @xlPrevPrdSales_Other.setter
    def xlPrevPrdSales_Other(self, param: float):
        self.__xlPrevPrdSales_Other = param

    @property
    def xlPrevPrdSalesRatio_1(self):
        return self.__xlPrevPrdSalesRatio_1

    @xlPrevPrdSalesRatio_1.setter
    def xlPrevPrdSalesRatio_1(self, param: float):
        self.__xlPrevPrdSalesRatio_1 = param

    @property
    def xlPrevPrdSalesRatio_2(self):
        return self.__xlPrevPrdSalesRatio_2

    @xlPrevPrdSalesRatio_2.setter
    def xlPrevPrdSalesRatio_2(self, param: float):
        self.__xlPrevPrdSalesRatio_2 = param

    @property
    def xlPrevPrdSalesRatio_3(self):
        return self.__xlPrevPrdSalesRatio_3

    @xlPrevPrdSalesRatio_3.setter
    def xlPrevPrdSalesRatio_3(self, param: float):
        self.__xlPrevPrdSalesRatio_3 = param

    @property
    def xlPrevPrdSalesRatio_4(self):
        return self.__xlPrevPrdSalesRatio_4

    @xlPrevPrdSalesRatio_4.setter
    def xlPrevPrdSalesRatio_4(self, param: float):
        self.__xlPrevPrdSalesRatio_4 = param

    @property
    def xlPrevPrdSalesRatio_5(self):
        return self.__xlPrevPrdSalesRatio_5

    @xlPrevPrdSalesRatio_5.setter
    def xlPrevPrdSalesRatio_5(self, param: float):
        self.__xlPrevPrdSalesRatio_5 = param

    @property
    def xlPrevPrdSalesRatio_Our(self):
        return self.__xlPrevPrdSalesRatio_Our

    @xlPrevPrdSalesRatio_Our.setter
    def xlPrevPrdSalesRatio_Our(self, param: float):
        self.__xlPrevPrdSalesRatio_Our = param

    @property
    def xlPrevPrdSalesRatio_Other(self):
        return self.__xlPrevPrdSalesRatio_Other

    @xlPrevPrdSalesRatio_Other.setter
    def xlPrevPrdSalesRatio_Other(self, param: float):
        self.__xlPrevPrdSalesRatio_Other = param

    @property
    def xlPrevPrdSales_Sum(self):
        return self.__xlPrevPrdSales_Sum

    @xlPrevPrdSales_Sum.setter
    def xlPrevPrdSales_Sum(self, param: float):
        self.__xlPrevPrdSales_Sum = param

    @property
    def xlPrevPrdOperatingProfit(self):
        return self.__xlPrevPrdOperatingProfit

    @xlPrevPrdOperatingProfit.setter
    def xlPrevPrdOperatingProfit(self, param: float):
        self.__xlPrevPrdOperatingProfit = param

    @property
    def xlPrevPrdOrdinaryIncome(self):
        return self.__xlPrevPrdOrdinaryIncome

    @xlPrevPrdOrdinaryIncome.setter
    def xlPrevPrdOrdinaryIncome(self, param: float):
        self.__xlPrevPrdOrdinaryIncome = param

    @property
    def xlLastPrdYear(self):
        return self.__xlLastPrdYear

    @xlLastPrdYear.setter
    def xlLastPrdYear(self, param: str):
        self.__xlLastPrdYear = param

    @property
    def xlLastPrdSales_1(self):
        return self.__xlLastPrdSales_1

    @xlLastPrdSales_1.setter
    def xlLastPrdSales_1(self, param: float):
        self.__xlLastPrdSales_1 = param

    @property
    def xlLastPrdSales_2(self):
        return self.__xlLastPrdSales_2

    @xlLastPrdSales_2.setter
    def xlLastPrdSales_2(self, param: float):
        self.__xlLastPrdSales_2 = param

    @property
    def xlLastPrdSales_3(self):
        return self.__xlLastPrdSales_3

    @xlLastPrdSales_3.setter
    def xlLastPrdSales_3(self, param: float):
        self.__xlLastPrdSales_3 = param

    @property
    def xlLastPrdSales_4(self):
        return self.__xlLastPrdSales_4

    @xlLastPrdSales_4.setter
    def xlLastPrdSales_4(self, param: float):
        self.__xlLastPrdSales_4 = param

    @property
    def xlLastPrdSales_5(self):
        return self.__xlLastPrdSales_5

    @xlLastPrdSales_5.setter
    def xlLastPrdSales_5(self, param: float):
        self.__xlLastPrdSales_5 = param

    @property
    def xlLastPrdSales_Our(self):
        return self.__xlLastPrdSales_Our

    @xlLastPrdSales_Our.setter
    def xlLastPrdSales_Our(self, param: float):
        self.__xlLastPrdSales_Our = param

    @property
    def xlLastPrdSales_Other(self):
        return self.__xlLastPrdSales_Other

    @xlLastPrdSales_Other.setter
    def xlLastPrdSales_Other(self, param: float):
        self.__xlLastPrdSales_Other = param

    @property
    def xlLastPrdSalesRatio_1(self):
        return self.__xlLastPrdSalesRatio_1

    @xlLastPrdSalesRatio_1.setter
    def xlLastPrdSalesRatio_1(self, param: float):
        self.__xlLastPrdSalesRatio_1 = param

    @property
    def xlLastPrdSalesRatio_2(self):
        return self.__xlLastPrdSalesRatio_2

    @xlLastPrdSalesRatio_2.setter
    def xlLastPrdSalesRatio_2(self, param: float):
        self.__xlLastPrdSalesRatio_2 = param

    @property
    def xlLastPrdSalesRatio_3(self):
        return self.__xlLastPrdSalesRatio_3

    @xlLastPrdSalesRatio_3.setter
    def xlLastPrdSalesRatio_3(self, param: float):
        self.__xlLastPrdSalesRatio_3 = param

    @property
    def xlLastPrdSalesRatio_4(self):
        return self.__xlLastPrdSalesRatio_4

    @xlLastPrdSalesRatio_4.setter
    def xlLastPrdSalesRatio_4(self, param: float):
        self.__xlLastPrdSalesRatio_4 = param

    @property
    def xlLastPrdSalesRatio_5(self):
        return self.__xlLastPrdSalesRatio_5

    @xlLastPrdSalesRatio_5.setter
    def xlLastPrdSalesRatio_5(self, param: float):
        self.__xlLastPrdSalesRatio_5 = param

    @property
    def xlLastPrdSalesRatio_Our(self):
        return self.__xlLastPrdSalesRatio_Our

    @xlLastPrdSalesRatio_Our.setter
    def xlLastPrdSalesRatio_Our(self, param: float):
        self.__xlLastPrdSalesRatio_Our = param

    @property
    def xlLastPrdSalesRatio_Other(self):
        return self.__xlLastPrdSalesRatio_Other

    @xlLastPrdSalesRatio_Other.setter
    def xlLastPrdSalesRatio_Other(self, param: float):
        self.__xlLastPrdSalesRatio_Other = param

    @property
    def xlLastPrdSales_Sum(self):
        return self.__xlLastPrdSales_Sum

    @xlLastPrdSales_Sum.setter
    def xlLastPrdSales_Sum(self, param: float):
        self.__xlLastPrdSales_Sum = param

    @property
    def xlLastPrdOperatingProfit(self):
        return self.__xlLastPrdOperatingProfit

    @xlLastPrdOperatingProfit.setter
    def xlLastPrdOperatingProfit(self, param: float):
        self.__xlLastPrdOperatingProfit = param

    @property
    def xlLastPrdOrdinaryIncome(self):
        return self.__xlLastPrdOrdinaryIncome

    @xlLastPrdOrdinaryIncome.setter
    def xlLastPrdOrdinaryIncome(self, param: float):
        self.__xlLastPrdOrdinaryIncome = param

    @property
    def xlCurPrdMainProducts(self):
        return self.__xlCurPrdMainProducts

    @xlCurPrdMainProducts.setter
    def xlCurPrdMainProducts(self, param: str):
        self.__xlCurPrdMainProducts = param

    @property
    def xlMainSupplier_1(self):
        return self.__xlMainSupplier_1

    @xlMainSupplier_1.setter
    def xlMainSupplier_1(self, param: str):
        self.__xlMainSupplier_1 = param

    @property
    def xlMainSupplier_2(self):
        return self.__xlMainSupplier_2

    @xlMainSupplier_2.setter
    def xlMainSupplier_2(self, param: str):
        self.__xlMainSupplier_2 = param

    @property
    def xlMainSupplier_3(self):
        return self.__xlMainSupplier_3

    @xlMainSupplier_3.setter
    def xlMainSupplier_3(self, param: str):
        self.__xlMainSupplier_3 = param

    @property
    def xlMainSupplier_4(self):
        return self.__xlMainSupplier_4

    @xlMainSupplier_4.setter
    def xlMainSupplier_4(self, param: str):
        self.__xlMainSupplier_4 = param

    @property
    def xlMainSupplier_5(self):
        return self.__xlMainSupplier_5

    @xlMainSupplier_5.setter
    def xlMainSupplier_5(self, param: str):
        self.__xlMainSupplier_5 = param

    @property
    def xlMainSupplierValue_1(self):
        return self.__xlMainSupplierValue_1

    @xlMainSupplierValue_1.setter
    def xlMainSupplierValue_1(self, param: float):
        self.__xlMainSupplierValue_1 = param

    @property
    def xlMainSupplierValue_2(self):
        return self.__xlMainSupplierValue_2

    @xlMainSupplierValue_2.setter
    def xlMainSupplierValue_2(self, param: float):
        self.__xlMainSupplierValue_2 = param

    @property
    def xlMainSupplierValue_3(self):
        return self.__xlMainSupplierValue_3

    @xlMainSupplierValue_3.setter
    def xlMainSupplierValue_3(self, param: float):
        self.__xlMainSupplierValue_3 = param

    @property
    def xlMainSupplierValue_4(self):
        return self.__xlMainSupplierValue_4

    @xlMainSupplierValue_4.setter
    def xlMainSupplierValue_4(self, param: float):
        self.__xlMainSupplierValue_4 = param

    @property
    def xlMainSupplierValue_5(self):
        return self.__xlMainSupplierValue_5

    @xlMainSupplierValue_5.setter
    def xlMainSupplierValue_5(self, param: float):
        self.__xlMainSupplierValue_5 = param

    @property
    def xlMainSupplierRatio_1(self):
        return self.__xlMainSupplierRatio_1

    @xlMainSupplierRatio_1.setter
    def xlMainSupplierRatio_1(self, param: float):
        self.__xlMainSupplierRatio_1 = param

    @property
    def xlMainSupplierRatio_2(self):
        return self.__xlMainSupplierRatio_2

    @xlMainSupplierRatio_2.setter
    def xlMainSupplierRatio_2(self, param: float):
        self.__xlMainSupplierRatio_2 = param

    @property
    def xlMainSupplierRatio_3(self):
        return self.__xlMainSupplierRatio_3

    @xlMainSupplierRatio_3.setter
    def xlMainSupplierRatio_3(self, param: float):
        self.__xlMainSupplierRatio_3 = param

    @property
    def xlMainSupplierRatio_4(self):
        return self.__xlMainSupplierRatio_4

    @xlMainSupplierRatio_4.setter
    def xlMainSupplierRatio_4(self, param: float):
        self.__xlMainSupplierRatio_4 = param

    @property
    def xlMainSupplierRatio_5(self):
        return self.__xlMainSupplierRatio_5

    @xlMainSupplierRatio_5.setter
    def xlMainSupplierRatio_5(self, param: float):
        self.__xlMainSupplierRatio_5 = param

    @property
    def xlMainProducts_1(self):
        return self.__xlMainProducts_1

    @xlMainProducts_1.setter
    def xlMainProducts_1(self, param: str):
        self.__xlMainProducts_1 = param

    @property
    def xlMainProducts_2(self):
        return self.__xlMainProducts_2

    @xlMainProducts_2.setter
    def xlMainProducts_2(self, param: str):
        self.__xlMainProducts_2 = param

    @property
    def xlMainProducts_3(self):
        return self.__xlMainProducts_3

    @xlMainProducts_3.setter
    def xlMainProducts_3(self, param: str):
        self.__xlMainProducts_3 = param

    @property
    def xlMainProducts_4(self):
        return self.__xlMainProducts_4

    @xlMainProducts_4.setter
    def xlMainProducts_4(self, param: str):
        self.__xlMainProducts_4 = param

    @property
    def xlMainProducts_5(self):
        return self.__xlMainProducts_5

    @xlMainProducts_5.setter
    def xlMainProducts_5(self, param: str):
        self.__xlMainProducts_5 = param
