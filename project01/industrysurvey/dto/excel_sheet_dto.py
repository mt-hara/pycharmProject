from abstractdto.abs_excel_sheet_dto import AbstractExcelSheetDTO
class ExcelSheetDTO(AbstractExcelSheetDTO):
    def __init__(self, ws):
        super().__init__()
        self.xlCustomerCd = self.celldata(ws.range("H3").value, str)  # H3
        self.xlCustomerName = self.celldata(ws.range("H5").value, str)  # H5
        # self.__xlCustomerKanaName: str = ""  # H4
        # self.__xlHeadOfficeZipCd: str = ""  # I7
        # self.__xlHeadOfficeAddress: str = ""  # H8
        # self.__xlHeadOfficeTel: str = ""  # X7
        # self.__xlHeadOfficeFax: str = ""  # AH7
        # self.__xlBranchOfficeZipCd: str = ""  # I10
        # self.__xlBranchOfficeAddress: str = ""  # H11
        # self.__xlBranchOfficeTel: str = ""  # X10
        # self.__xlBranchOfficeFax: str = ""  # AH10
        # self.__xlRepName: str = ""  # H14
        # self.__xlRepKanaName: str = ""  # H13
        # self.__xlRepJobTitle: str = ""  # AD13
        # self.__xlRepBirthYear: str = ""  # AD14
        # self.__xlRepBirthMonth: str = ""  # AH14
        # self.__xlRepBirthDay: str = ""  # AK14
        # self.__xlEmployees: int = 0  # k22
        # self.__xlEmployeeYear: str = ""  # I23
        # self.__xlEmployeeMonth: str = ""  # O23
        self.__xlCapitalForm: int = 0  # shape 取得
        self.__xlCorporateType: str = ""  # shape 取得
        # self.__xlCustomerCapital: float = 0  # H18
        # self.__xlEstablishedYear: str = ""  # O19
        # self.__xlEstablishedMonth: str = ""  # I19
        # self.__xlAccountClosingMonth: int = 0  # M21
        # self.__xlReturnOnEquity: float = 0  # I20
        self.__xlISO9001Certif: str = ""  # D50 shape 取得 取得済 取得予定 取得予定なし
        self.__xlISO9001Plan: str = ""  # D51
        self.__xlISO9001NoCertif: str = ""  # D52
        # self.__xlISO9001ResistedNo: str = ""  # N50
        # self.__xlISO9001CertifPlanYear: str = ""  # N51
        # self.__xlISO9001CertifPlanMonth: str = ""  # R51
        self.__xlISO14001Certif: str = ""  # V50 shape 取得 取得 取得済 取得予定 取得予定なし
        self.__xlISO14001Plan: str = ""  # V51
        self.__xlISO14001NoCertif: str = ""  # V52
        # self.__xlISO14001ResistedNo: str = ""  # AF50
        # self.__xlISO14001CertifPlanYear: str = ""  # AF51
        # self.__xlISO14001CertifPlanMonth: str = ""  # AJ51
        # self.__xlOtherCertif: str = ""  # I53
        self.__xlCustomerBizType: int = 0  # shape 取得
        # self.__xlOtherBizType: str = ""  # 手入力
        # self.__xlPicName: str = ""  # H57
        # self.__xlPicEmailAddress: str = ""  # H58
        # self.__xlpicDept: str = ""  # H59
        # self.__xlpicPosition: str = ""  # G59
        # self.__xlContactZipCd: str = ""  # H55
        # self.__xlContactAddress: str = ""  # C56
        # self.__xlContactTel: str = ""  # H60
        # self.__xlContactFax: str = ""  # G60
        self.__xlStockListingStatus: int = 0  # 0:非上場　1:上場 shape 取得
        self.__xlStockMarket: str = ""  # shape 取得 Text
        # self.__xlMainStockholder_1: str = ""  # U19
        # self.__xlMainStockholder_2: str = ""  # U20
        # self.__xlMainStockholder_3: str = ""  # U21
        # self.__xlMainStockholder_4: str = ""  # U22
        # self.__xlMainStockholder_5: str = ""  # U23
        # self.__xlRatioSH_1: float = 0  # AK19
        # self.__xlRatioSH_2: float = 0  # AK20
        # self.__xlRatioSH_3: float = 0  # AK21
        # self.__xlRatioSH_4: float = 0  # AK22
        # self.__xlRatioSH_5: float = 0  # AK23
        # self.__xlmainCustomer_1: str = ""  # C28
        # self.__xlmainCustomer_2: str = ""  # C29
        # self.__xlmainCustomer_3: str = ""  # C30
        # self.__xlmainCustomer_4: str = ""  # C31
        # self.__xlmainCustomer_5: str = ""  # C32
        # self.__xlCurPrdYear: str = ""  # M26
        # self.__xlCurPrdSales_1: float = 0  # M28
        # self.__xlCurPrdSales_2: float = 0  # M29
        # self.__xlCurPrdSales_3: float = 0  # M30
        # self.__xlCurPrdSales_4: float = 0  # M31
        # self.__xlCurPrdSales_5: float = 0  # M32
        # self.__xlCurPrdSales_Our: float = 0  # M34
        # self.__xlCurPrdSales_Other: float = 0  # M33
        # self.__xlCurPrdSalesRatio_1: float = 0  # S28
        # self.__xlCurPrdSalesRatio_2: float = 0  # S29
        # self.__xlCurPrdSalesRatio_3: float = 0  # S30
        # self.__xlCurPrdSalesRatio_4: float = 0  # S31
        # self.__xlCurPrdSalesRatio_5: float = 0  # S32
        # self.__xlCurPrdSalesRatio_Our: float = 0  # S34
        # self.__xlCurPrdSalesRatio_Othor: float = 0  # S33
        # self.__xlCurPrdSales_Sum: float = 0  # M35
        # self.__xlCurPrdOperatingProfit: float = 0  # M36
        # self.__xlCurPrdOrdinaryIncome: float = 0  # M37
        # self.__xlPrevPrdYear: str = ""  # V26
        # self.__xlPrevPrdSales_1: float = 0  # V28
        # self.__xlPrevPrdSales_2: float = 0  # V29
        # self.__xlPrevPrdSales_3: float = 0  # V30
        # self.__xlPrevPrdSales_4: float = 0  # V31
        # self.__xlPrevPrdSales_5: float = 0  # V32
        # self.__xlPrevPrdSales_Our: float = 0  # V34
        # self.__xlPrevPrdSales_Other: float = 0  # V33
        # self.__xlPrevPrdSalesRatio_1: float = 0  # AB28
        # self.__xlPrevPrdSalesRatio_2: float = 0  # AB29
        # self.__xlPrevPrdSalesRatio_3: float = 0  # AB30
        # self.__xlPrevPrdSalesRatio_4: float = 0  # AB31
        # self.__xlPrevPrdSalesRatio_5: float = 0  # AB32
        # self.__xlPrevPrdSalesRatio_Our: float = 0  # AB34
        # self.__xlPrevPrdSalesRatio_Other: float = 0  # AB33
        # self.__xlPrevPrdSales_Sum: float = 0  # V35
        # self.__xlPrevPrdOperatingProfit: float = 0  # V36
        # self.__xlPrevPrdOrdinaryIncome: float = 0  # V37
        # self.__xlLastPrdYear: str = ""  # AE26
        # self.__xlLastPrdSales_1: float = 0  # AE28
        # self.__xlLastPrdSales_2: float = 0  # AE29
        # self.__xlLastPrdSales_3: float = 0  # AE30
        # self.__xlLastPrdSales_4: float = 0  # AE31
        # self.__xlLastPrdSales_5: float = 0  # AE32
        # self.__xlLastPrdSales_Our: float = 0  # AE34
        # self.__xlLastPrdSales_Other: float = 0  # AE33
        # self.__xlLastPrdSalesRatio_1: float = 0  # AK28
        # self.__xlLastPrdSalesRatio_2: float = 0  # AK29
        # self.__xlLastPrdSalesRatio_3: float = 0  # AK30
        # self.__xlLastPrdSalesRatio_4: float = 0  # AK31
        # self.__xlLastPrdSalesRatio_5: float = 0  # AK32
        # self.__xlLastPrdSalesRatio_Our: float = 0  # AK34
        # self.__xlLastPrdSalesRatio_Other: float = 0  # AK33
        # self.__xlLastPrdSales_sum: float = 0  # AE35
        # self.__xlLastPrdOperatingProfit: float = 0  # AE36
        # self.__xlLastPrdOrdinaryIncome: float = 0  # AE37
        # self.__xlCurPrdMainProducts: str = ""  # M38
        # self.__xlMainSupplier_1: str = ""  # W42
        # self.__xlMainSupplier_2: str = ""  # W43
        # self.__xlMainSupplier_3: str = ""  # W44
        # self.__xlMainSupplier_4: str = ""  # W45
        # self.__xlMainSupplier_5: str = ""  # W46
        # self.__xlMainSupplierValue_1: float = 0  # AG42
        # self.__xlMainSupplierValue_2: float = 0  # AG43
        # self.__xlMainSupplierValue_3: float = 0  # AG44
        # self.__xlMainSupplierValue_4: float = 0  # AG45
        # self.__xlMainSupplierValue_5: float = 0  # AG46
        # self.__xlMainSupplierRatio_1: float = 0  # AK42
        # self.__xlMainSupplierRatio_2: float = 0  # AK43
        # self.__xlMainSupplierRatio_3: float = 0  # AK44
        # self.__xlMainSupplierRatio_4: float = 0  # AK45
        # self.__xlMainSupplierRatio_5: float = 0  # AK46
        # self.__xlMainProducts_1: str = ""  # C42
        # self.__xlMainProducts_2: str = ""  # C43
        # self.__xlMainProducts_3: str = ""  # C44
        # self.__xlMainProducts_4: str = ""  # C45
        # self.__xlMainProducts_5: str = ""  # C46




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


    def select_shapes_field(self,fieldname,data):
        pass