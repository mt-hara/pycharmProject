from abstractdto.abs_excel_sheet_dto import AbstractExcelSheetDTO


class ExcelSheetDTO(AbstractExcelSheetDTO):
    def __init__(self, ws):
        super(ExcelSheetDTO, self).__init__()
        self.ws = ws
        self.xlCustomerCd: str = self.cells("H3", str)  # H3
        self.xlCustomerName: str = self.cells("H5", str)  # H5
        self.xlCustomerKanaName: str = self.cells("H4", str)  # H4
        self.xlHeadOfficeZipCd: str = self.cells("I7", str)  # I7
        self.xlHeadOfficeAddress: str = self.cells("H8", str)  # H8
        self.xlHeadOfficeTel: str = self.cells("X7", str)  # X7
        self.xlHeadOfficeFax: str = self.cells("AH7", str)  # AH7
        self.xlBranchOfficeZipCd: str = self.cells("I10", str)  # I10
        self.xlBranchOfficeAddress: str = self.cells("H11", str)  # H11
        self.xlBranchOfficeTel: str = self.cells("X10", str)  # X10
        self.xlBranchOfficeFax: str = self.cells("AH10", str)  # AH10
        self.xlRepName: str = self.cells("H14", str)  # H14
        self.xlRepKanaName: str = self.cells("H13", str)  # H13
        self.xlRepJobTitle: str = self.cells("AD13", str)  # AD13
        self.xlRepBirthYear: str = self.cells("AD14", str)  # AD14
        self.xlRepBirthMonth: str = self.cells("AH14", str)  # AH14
        self.xlRepBirthDay: str = self.cells("AK14", str)  # AK14
        self.xlEmployees: int = self.cells("K22", int)  # K22
        self.xlEmployeeYear: str = self.cells("I23", str)  # I23
        self.xlEmployeeMonth: str = self.cells("O23", str)  # O23
        self.xlCustomerCapital: float = self.cells("H18", float)  # H18
        self.xlEstablishedYear: str = self.cells("O19", str)  # O19
        self.xlEstablishedMonth: str = self.cells("I19", str)  # I19
        self.xlAccountClosingMonth: int = self.cells("M21", int)  # M21
        self.xlReturnOnEquity: float = self.cells("I20", float)  # I20
        self.xlISO9001Certif: str = self.cells("D50", str)  # D50 shape or cell
        self.xlISO9001Plan: str = self.cells("D51", str)  # D51 shape or cell
        self.xlISO9001NoCertif: str = self.cells("D52", str)  # D52 shape or cell
        self.xlISO9001ResistedNo: str = self.cells("N50", str)  # N50
        self.xlISO9001CertifPlanYear: str = self.cells("N51", str)  # N51
        self.xlISO9001CertifPlanMonth: str = self.cells("R51", str)  # R51
        self.xlISO14001Certif: str = self.cells("V50", str)  # V50 shape or cell
        self.xlISO14001Plan: str = self.cells("V51", str)  # V51 shape or cell
        self.xlISO14001NoCertif: str = self.cells("V52", str)  # V52 shape or cell
        self.xlISO14001ResistedNo: str = self.cells("AF50", str)  # AF50
        self.xlISO14001CertifPlanYear: str = self.cells("AF51", str)  # AF52
        self.xlISO14001CertifPlanMonth: str = self.cells("AJ51", str)  # AJ51
        self.xlOtherCertif: str = self.cells("I53", str)  # I53
        self.xlOtherBizType: str = ""
        self.xlPicName: str = self.cells("H57", str)  # H57
        self.xlPicEmailAddress: str = self.cells("H58", str)  # H58
        self.xlPicDept: str = self.cells("H59", str)  # H59
        self.xlPicPosition: str = self.cells("G59", str)  # G59
        self.xlContactZipCd: str = self.cells("H55", str)  # H55
        self.xlContactAddress: str = self.cells("C56", str)  # C56
        self.xlContactTel: str = self.cells("H60", str)  # H60
        self.xlContactFax: str = self.cells("G60", str)  # G60
        self.xlMainStockholder_1: str = self.cells("U19", str)  # U19
        self.xlMainStockholder_2: str = self.cells("U20", str)  # U20
        self.xlMainStockholder_3: str = self.cells("U21", str)  # U21
        self.xlMainStockholder_4: str = self.cells("U22", str)  # U22
        self.xlMainStockholder_5: str = self.cells("U23", str)  # U23
        self.xlRatioSH_1: float = self.cells("AK19", float)  # AK19
        self.xlRatioSH_2: float = self.cells("AK20", float)  # AK20
        self.xlRatioSH_3: float = self.cells("AK21", float)  # AK21
        self.xlRatioSH_4: float = self.cells("AK22", float)  # AK22
        self.xlRatioSH_5: float = self.cells("AK23", float)  # AK23
        self.xlmainCustomer_1: str = self.cells("C28", str)  # C28
        self.xlmainCustomer_2: str = self.cells("C29", str)  # C29
        self.xlmainCustomer_3: str = self.cells("C30", str)  # C30
        self.xlmainCustomer_4: str = self.cells("C31", str)  # C31
        self.xlmainCustomer_5: str = self.cells("C32", str)  # C32
        self.xlCurPrdYear: str = self.cells("M26", str)  # M26
        self.xlCurPrdSales_1: int = self.cells("M28", int)  # M28
        self.xlCurPrdSales_2: int = self.cells("M29", int)  # M29
        self.xlCurPrdSales_3: int = self.cells("M30", int)  # M30
        self.xlCurPrdSales_4: int = self.cells("M31", int)  # M31
        self.xlCurPrdSales_5: int = self.cells("M32", int)  # M32
        self.xlCurPrdSales_Our: int = self.cells("M34", int)  # M34
        self.xlCurPrdSales_Other: int = self.cells("M33", int)  # M33
        self.xlCurPrdSalesRatio_1: float = self.cells("S28", float)  # S28
        self.xlCurPrdSalesRatio_2: float = self.cells("S29", float)  # S29
        self.xlCurPrdSalesRatio_3: float = self.cells("S30", float)  # S30
        self.xlCurPrdSalesRatio_4: float = self.cells("S31", float)  # S31
        self.xlCurPrdSalesRatio_5: float = self.cells("S32", float)  # S32
        self.xlCurPrdSalesRatio_Our: float = self.cells("S34", float)  # S34
        self.xlCurPrdSalesRatio_Othor: float = self.cells("S33", float)  # S33





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

    #        self.__xlCapitalForm: int = 0  # shape 取得
    #        self.__xlCorporateType: str = ""  # shape 取得
    #        self.__xlCustomerBizType: int = 0  # shape 取得
    #        self.__xlStockListingStatus: int = 0  # 0:非上場　1:上場 shape 取得
    #        self.__xlStockMarket: str = ""  # shape 取得 Text

    def __get_cell(self, range_value: str):
        return self.ws.range(range_value).value

    def cells(self, range_value: str, datatype):
        param = self.__get_cell(range_value)
        # cellのデータ型とDTOのデータ型の整合性を取る
        if param == None:
            return None
        # cellのデータ型がInt or floatの場合
        elif type(param) == int or type(param) == float:
            if datatype == int:
                return int(param)
            elif datatype == float:
                return float(param)
            elif datatype == str:
                # 小数点以下を削除
                return str(int(param))
        # 上記以外の場合
        else:
            if datatype == int:
                return int(param)
            elif datatype == float:
                return float(param)
            elif datatype == str:
                return str(param)

    # def celldata(self, param, datatype):
    #     if param == None:
    #         return None
    #     elif type(param) == int or type(param) == float:
    #         if datatype == int:
    #             return int(param)
    #         elif datatype == float:
    #             return float(param)
    #         elif datatype == str:
    #             # 小数点以下を削除
    #             return str(int(param))
    #     else:
    #         if datatype == int:
    #             return int(param)
    #         elif datatype == float:
    #             return float(param)
    #         elif datatype == str:
    #             return str(param)
