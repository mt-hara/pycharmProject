class ExcelSheetDTO():
    def __init__(self, ws):
        self.__xlCustomerCd: str = self.celldata(ws.range("H3").value, str)  # H3
        self.__xlCustomerName: str = self.celldata(ws.range("H5").value, str)  # H5
        self.__xlCustomerKanaName: str = self.celldata(ws.range("H4").value, str)  # H4
        self.__xlHeadOfficeZipCd: str = self.celldata(ws.range("I7").value, str)  # I7
        self.__xlHeadOfficeAddress: str = self.celldata(ws.range("H8").value, str)  # H8
        self.__xlHeadOfficeTel: str = self.celldata(ws.range("X7").value, str)  # X7
        self.__xlHeadOfficeFax: str = self.celldata(ws.range("AH7").value, str)  # AH7
        self.__xlBranchOfficeZipCd: str = self.celldata(ws.range("I10").value, str)  # I10
        self.__xlBranchOfficeAddress: str = self.celldata(ws.range("H11").value, str)  # H11
        self.__xlBranchOfficeTel: str = self.celldata(ws.range("X10").value, str)  # X10
        self.__xlBranchOfficeFax: str = self.celldata(ws.range("AH10").value, str)  # AH10
        self.__xlRepName: str = self.celldata(ws.range("H14").value, str)  # H14
        self.__xlRepKanaName: str = self.celldata(ws.range("H13").value, str)  # H13
        self.__xlRepJobTitle: str = self.celldata(ws.range("AD13").value, str)  # AD13
        self.__xlRepBirthYear: str = self.celldata(ws.range("AD14").value, str)  # AD14
        self.__xlRepBirthMonth: str = self.celldata(ws.range("AH14").value, str)  # AH14
        self.__xlRepBirthDay: str = self.celldata(ws.range("AK14").value, str)  # AK14
        self.__xlEmployees: int = self.celldata(ws.range("K22").value, int)  # k22
        self.__xlEmployeeYear: str = self.celldata(ws.range("I23").value, str)  # I23
        self.__xlEmployeeMonth: int = self.celldata(ws.range("O23").value, int)  # O23
        self.__xlCapitalForm: int = None  # shape 取得
        self.__xlCorporateType: str = ""  # shape 取得
        self.__xlCustomerCapital: float = self.celldata(ws.range("H18").value, float)  # H18
        self.__xlEstablishedMonth: str = self.celldata(ws.range("I19").value, str)  # I19
        self.__xlEstablishedYear: int = self.celldata(ws.range("O19").value, int)  # O19
        self.__xlAccountClosingMonth: int = self.celldata(ws.range("M21").value, int)  # M21
        self.__xlReturnOnEquity: float = self.celldata(ws.range("I20").value, float)  # I20
        self.__xlISO9001Certif: str = self.celldata(ws.range("D50").value, str)  # D50 shape 取得 取得済 取得予定 取得予定なし
        self.__xlISO9001Plan: str = self.celldata(ws.range("D51").value, str)  # D51
        self.__xlISO9001NoCertif: str = self.celldata(ws.range("D52").value, str)  # D52
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
        #     CustomerCategory: str  # ""
        self.__xlCustomerBizType: int = None  # shape 取得
        self.__xlPicName: str = ""  # H57
        self.__xlPicEmailAddress: str = ""  # H58
        self.__xlpicDept: str = ""  # H59
        self.__xlpicPosition: str = ""  # G59
        self.__xlContactZipCd: str = ""  # H55
        self.__xlContactAddress: str = ""  # C56
        self.__xlContactTel: str = ""  # H60
        self.__xlContactFax: str  # G60
        self.__xlStockListingStatus: int  # 0:非上場　1:上場 shape 取得
        self.__xlStockMarket: str  # shape 取得 Text
        self.__xlMainStockholder_1: str  # U19
        self.__xlMainStockholder_2: str  # U20
        self.__xlMainStockholder_3: str  # U21
        self.__xlMainStockholder_4: str  # U22
        self.__xlMainStockholder_5: str  # U23
        self.__xlRatioSH_1: float  # AK19
        self.__xlRatioSH_2: float  # AK20
        self.__xlRatioSH_3: float  # AK21
        self.__xlRatioSH_4: float  # AK22
        self.__xlRatioSH_5: float  # AK23
        self.__xlmainCustomer_1: str  # C28
        self.__xlmainCustomer_2: str  # C29
        self.__xlmainCustomer_3: str  # C30
        self.__xlmainCustomer_4: str  # C31
        self.__xlmainCustomer_5: str  # C32
        self.__xlCurPrdYear: str  # M26
        self.__xlCurPrdSales_1: float  # M28
        self.__xlCurPrdSales_2: float  # M29
        self.__xlCurPrdSales_3: float  # M30
        self.__xlCurPrdSales_4: float  # M31
        self.__xlCurPrdSales_5: float  # M32
        self.__xlCurPrdSales_Our: float  # M34
        self.__xlCurPrdSales_Other: float  # M33
        self.__xlCurPrdSalesRatio_1: float  # S28
        self.__xlCurPrdSalesRatio_2: float  # S29
        self.__xlCurPrdSalesRatio_3: float  # S30
        self.__xlCurPrdSalesRatio_4: float  # S31
        self.__xlCurPrdSalesRatio_5: float  # S32
        self.__xlCurPrdSalesRatio_Our: float  # S34
        self.__xlCurPrdSalesRatio_Othor: float  # S33
        self.__xlCurPrdSales_Sum: float  # M35
        self.__xlCurPrdOperatingProfit: float  # M36
        self.__xlCurPrdOrdinaryincome: float  # M37
        self.__xlPrevPrdYear: str  # V26
        self.__xlPrevPrdSales_1: float  # V28
        self.__xlPrevPrdSales_2: float  # V29
        self.__xlPrevPrdSales_3: float  # V30
        self.__xlPrevPrdSales_4: float  # V31
        self.__xlPrevPrdSales_5: float  # V32
        self.__xlPrevPrdSales_Our: float  # V34
        self.__xlPrevPrdSales_Other: float  # V33
        self.__xlPrevPrdSalesRatio_1: float  # AB28
        self.__xlPrevPrdSalesRatio_2: float  # AB29
        self.__xlPrevPrdSalesRatio_3: float  # AB30
        self.__xlPrevPrdSalesRatio_4: float  # AB31
        self.__xlPrevPrdSalesRatio_5: float  # AB32
        self.__xlPrevPrdSalesRatio_Our: float  # AB34
        self.__xlPrevPrdSalesRatio_Other: float  # AB33
        self.__xlPrevPrdSales_Sum: float  # V35
        self.__xlPrevPrdOperatingProfit: float  # V36
        self.__xlPrevPrdOrdinaryIncome: float  # V37
        self.__xlLastPrdYear: str  # AE26
        self.__xlLastPrdSales_1: float  # AE28
        self.__xlLastPrdSales_2: float  # AE29
        self.__xlLastPrdSales_3: float  # AE30
        self.__xlLastPrdSales_4: float  # AE31
        self.__xlLastPrdSales_5: float  # AE32
        self.__xlLastPrdSales_Our: float  # AE34
        self.__xlLastPrdSales_Other: float  # AE33
        self.__xlLastPrdSalesRatio_1: float  # AK28
        self.__xlLastPrdSalesRatio_2: float  # AK29
        self.__xlLastPrdSalesRatio_3: float  # AK30
        self.__xlLastPrdSalesRatio_4: float  # AK31
        self.__xlLastPrdSalesRatio_5: float  # AK32
        self.__xlLastPrdSalesRatio_Our: float  # AK34
        self.__xlLastPrdSalesRatio_Other: float  # AK33
        self.__xlLastPrdSales_sum: float  # AE35
        self.__xlLastPrdOperatingProfit: float  # AE36
        self.__xlLastPrdOrdinaryincome: float  # AE37
        self.__xlCurPrdMainProducts: str  # M38
        self.__xlMainSupplier_1: str  # W42
        self.__xlMainSupplier_2: str  # W43
        self.__xlMainSupplier_3: str  # W44
        self.__xlMainSupplier_4: str  # W45
        self.__xlMainSupplier_5: str  # W46
        self.__xlMainSupplierValue_1: float  # AG42
        self.__xlMainSupplierValue_2: float  # AG43
        self.__xlMainSupplierValue_3: float  # AG44
        self.__xlMainSupplierValue_4: float  # AG45
        self.__xlMainSupplierValue_5: float  # AG46
        self.__xlMainSupplierRatio_1: float  # AK42
        self.__xlMainSupplierRatio_2: float  # AK43
        self.__xlMainSupplierRatio_3: float  # AK44
        self.__xlMainSupplierRatio_4: float  # AK45
        self.__xlMainSupplierRatio_5: float  # AK46
        self.__xlMainProducts_1: str  # C42
        self.__xlMainProducts_2: str  # C43
        self.__xlMainProducts_3: str  # C44
        self.__xlMainProducts_4: str  # C45
        self.__xlMainProducts_5: str  # C46

    @property
    def xlCustomerCd(self):
        return self.__xlCustomerCd

    @xlCustomerCd.setter
    def xlCustomerCd(self, param):
        self.__xlCustomerCd = param

    def celldata(self, param, datatype):
        if param == None:
            return None
        elif type(param) == int or type(param) == float:
            if datatype == int:
                return int(param)
            elif datatype == float:
                return float(param)
            elif datatype == str:
                # 小数点以下を削除
                return str(int(param))
        else:
            if datatype == int:
                return int(param)
            elif datatype == float:
                return float(param)
            elif datatype == str:
                return str(param)