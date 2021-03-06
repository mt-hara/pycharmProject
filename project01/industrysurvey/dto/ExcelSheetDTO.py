from dto.AbstractExcelSheetDTO import AbstractExcelSheetDTO
from excelapp.ShapeState import ShapesPosToValue
from abc import ABCMeta, abstractmethod
import re
import unicodedata

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
        self.xlCustomerCapital: float = self.cells_capital("H18") # H18
        # self.xlCustomerCapital: float = self.cells("H18", float)/1000  # H18
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
        self.xlContactFax: str = self.cells("Q60", str)  # G60
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
        self.xlCurPrdSales_Sum: int = self.cells("M35", int)  # M35
        self.xlCurPrdOperatingProfit: int = self.cells("M36", int)  # M36
        self.xlCurPrdOrdinaryIncome: int = self.cells("M37", int)  # M37
        self.xlPrevPrdYear: str = self.cells("V26", str)  # V26
        self.xlPrevPrdSales_1: int = self.cells("V28", int)  # V28
        self.xlPrevPrdSales_2: int = self.cells("V29", int)  # V29
        self.xlPrevPrdSales_3: int = self.cells("V30", int)  # V30
        self.xlPrevPrdSales_4: int = self.cells("V31", int)  # V31
        self.xlPrevPrdSales_5: int = self.cells("V32", int)  # V32
        self.xlPrevPrdSales_Our: int = self.cells("V34", int)  # V34
        self.xlPrevPrdSales_Other: int = self.cells("V33", int)  # V33
        self.xlPrevPrdSalesRatio_1: float = self.cells("AB28", float)  # AB28
        self.xlPrevPrdSalesRatio_2: float = self.cells("AB29", float)  # AB29
        self.xlPrevPrdSalesRatio_3: float = self.cells("AB30", float)  # AB30
        self.xlPrevPrdSalesRatio_4: float = self.cells("AB31", float)  # AB31
        self.xlPrevPrdSalesRatio_5: float = self.cells("AB32", float)  # AB32
        self.xlPrevPrdSalesRatio_Our: float = self.cells("AB34", float)  # AB34
        self.xlPrevPrdSalesRatio_Other: float = self.cells("AB33", float)  # AB33
        self.xlPrevPrdSales_Sum: int = self.cells("V35", int)  # V35
        self.xlPrevPrdOperatingProfit: int = self.cells("V36", int)  # V36
        self.xlPrevPrdOrdinaryIncome: int = self.cells("V37", int)  # V37
        self.xlLastPrdYear: str = self.cells("AE26", str)  # AE26
        self.xlLastPrdSales_1: int = self.cells("AE28", int)  # AE28
        self.xlLastPrdSales_2: int = self.cells("AE29", int)  # AE29
        self.xlLastPrdSales_3: int = self.cells("AE30", int)  # AE30
        self.xlLastPrdSales_4: int = self.cells("AE31", int)  # AE31
        self.xlLastPrdSales_5: int = self.cells("AE32", int)  # AE32
        self.xlLastPrdSales_Our: int = self.cells("AE34", int)  # AE34
        self.xlLastPrdSales_Other: int = self.cells("AE33", int)  # AE33
        self.xlLastPrdSalesRatio_1: float = self.cells("AK28", float)  # AK28
        self.xlLastPrdSalesRatio_2: float = self.cells("AK29", float)  # AK29
        self.xlLastPrdSalesRatio_3: float = self.cells("AK30", float)  # AK30
        self.xlLastPrdSalesRatio_4: float = self.cells("AK31", float)  # AK31
        self.xlLastPrdSalesRatio_5: float = self.cells("AK32", float)  # AK32
        self.xlLastPrdSalesRatio_Our: float = self.cells("AK34", float)  # AK34
        self.xlLastPrdSalesRatio_Other: float = self.cells("AK33", float)  # AK33
        self.xlLastPrdSales_Sum: int = self.cells("AE35", int)  # AE35
        self.xlLastPrdOperatingProfit: int = self.cells("AE36", int)  # AE36
        self.xlLastPrdOrdinaryIncome: int = self.cells("AE37", int)  # AE37
        self.xlCurPrdMainProducts: str = self.cells("M38", str)  # M38
        self.xlMainSupplier_1: str = self.cells("W42", str)  # W42
        self.xlMainSupplier_2: str = self.cells("W43", str)  # W43
        self.xlMainSupplier_3: str = self.cells("W44", str)  # W44
        self.xlMainSupplier_4: str = self.cells("W45", str)  # W45
        self.xlMainSupplier_5: str = self.cells("W46", str)  # W46
        self.xlMainSupplierValue_1: int = self.cells("AG42", int)  # AG42
        self.xlMainSupplierValue_2: int = self.cells("AG43", int)  # AG43
        self.xlMainSupplierValue_3: int = self.cells("AG44", int)  # AG44
        self.xlMainSupplierValue_4: int = self.cells("AG45", int)  # AG45
        self.xlMainSupplierValue_5: int = self.cells("AG46", int)  # AG46
        self.xlMainSupplierRatio_1: float = self.cells("AK42", float)  # AK42
        self.xlMainSupplierRatio_2: float = self.cells("AK43", float)  # AK43
        self.xlMainSupplierRatio_3: float = self.cells("AK44", float)  # AK44
        self.xlMainSupplierRatio_4: float = self.cells("AK45", float)  # AK45
        self.xlMainSupplierRatio_5: float = self.cells("AK46", float)  # AK46
        self.xlMainProducts_1: str = self.cells("C42", str)  # C42
        self.xlMainProducts_2: str = self.cells("C43", str)  # C43
        self.xlMainProducts_3: str = self.cells("C44", str)  # C44
        self.xlMainProducts_4: str = self.cells("C45", str)  # C45
        self.xlMainProducts_5: str = self.cells("C46", str)  # C46

        self.get_shapes_value()

    def __get_cell(self, range_value: str):
        return self.ws.range(range_value).value

    def cells_capital(self,range_value):
        param = self.__get_cell(range_value)
        if param == None:
            return None
        elif type(param) == int or type(param) == float:
            val = float(param)/1000
            return val

    def cells(self, range_value: str, datatype):
        param = self.__get_cell(range_value)
        # cellのデータ型とDTOのデータ型の整合性を取る
        if param == None:
            return None

        # if bool(re.compile("^\d+\.?\d*\Z").match(param)) == True:
        elif type(param) == int or type(param) == float:
            if datatype == int:
                return int(param)
            elif datatype == float:
                return float(param)
            elif datatype == str:
                # 小数点以下を削除
                tmp = str(int(param))
                # 前後の空白を削除
                s_param = self.strip_string(tmp)
                # 数字を半角、カタカナを全角に変換
                han_param = self.str_zen_han(s_param)
                return str(int(han_param))
        # 数値以外の場合でDTOのデータ型がSTR以外の場合はNoneを代入
        else:
            if datatype == str:
                han_param = self.str_zen_han(param)
                s_param = self.strip_string(han_param)
                return str(s_param)
            else:
                return None

    def str_zen_han(self,param):
        tmp = unicodedata.normalize("NFKC",param)
        return str(tmp)

    def strip_string(self,param: str):
        tmp = param.strip()
        return str(tmp)

    def get_shapes_value(self):
        shapes_data_factory = ShapesPosToValue(self.ws)
        self.shapes_dto = shapes_data_factory.shapes_dto
        self.xlCustomerBizType: str = self.shapes_dto.shCustomerBizType
        self.xlCapitalForm: str = self.shapes_dto.shCapitalForm
        self.xlCorporateType: str = self.shapes_dto.shCorporateType
        self.xlStockListingStatus: str = self.shapes_dto.shStockListingStatus
        self.xlStockMarket: str = self.shapes_dto.shStockMarket
        i_status = ISOCertifStatus()
        self.xlISO9001Certif = i_status.iso_status("certif", self.xlISO9001Certif, self.shapes_dto.shISO9001Certif)
        self.xlISO9001Plan = i_status.iso_status("plan", self.xlISO9001Plan, self.shapes_dto.shISO9001Plan)
        self.xlISO9001NoCertif = i_status.iso_status("no_certif", self.xlISO9001NoCertif, self.shapes_dto.shISO9001NoCertif)
        self.xlISO14001Certif = i_status.iso_status("certif", self.xlISO14001Certif, self.shapes_dto.shISO14001Certif)
        self.xlISO14001Plan = i_status.iso_status("plan", self.xlISO14001Plan, self.shapes_dto.shISO14001Plan)
        self.xlISO14001NoCertif = i_status.iso_status("no_certif", self.xlISO14001NoCertif, self.shapes_dto.shISO14001NoCertif)


class ISOCertifStatus():
    """
    ISO認証状況の選択パターンに応じて、セットする値を取得する。
    """
    def __init__(self):
        self.checktype = ""
        self.cellval = ""
        self.shapesval = ""

    def _set_iso_context_state(self, checktype, cellval, shapesval):
        self.checktype = checktype
        self.cellval =cellval
        self.shapesval = shapesval
        if checktype == "certif":
            return ISOCetif(self.cellval, self.shapesval)
        elif checktype == "plan":
            return ISOPlan(self.cellval, self.shapesval)
        elif checktype == "no_certif":
            return ISONoCertif(self.cellval, self.shapesval)

    def iso_status(self, checktype, cellval, shapesval):
        iso_context = self._set_iso_context_state(checktype, cellval, shapesval)
        return StateContext(iso_context).iso_value()


class ISOState(metaclass=ABCMeta):
    @abstractmethod
    def iso_value(self, state_context):
        pass


class ConcreteISOState(ISOState):
    def __init__(self, cellval, shapesval):
        self.cellVal = cellval
        self.shapeval = shapesval

    def iso_value(self, state_context):
        pass


class StateContext():
    def __init__(self, state_type):
        self.set_state(state_type)

    @property
    def current_state(self):
        return self.__current_state

    @current_state.setter
    def current_state(self, obj):
        self.current_state = obj

    def set_state(self, new_state):
        self.__current_state = new_state

    def iso_value(self):
        return self.current_state.iso_value(self)


class ISOCetif(ConcreteISOState):
    def __init__(self, cellval, shapesval):
        super().__init__(cellval, shapesval)
        self.iso_certif_val = ""

    def iso_value(self, state_context):
        if self.cellVal == "○" or self.cellVal is not None:
            self.iso_certif_val = "取得済"
        else:
            if self.shapeval  != "":
                self.iso_certif_val = "取得済"
            else:
                self.iso_certif_val = None

        return self.iso_certif_val


class ISOPlan(ConcreteISOState):
    def __init__(self, cellval, shapesval):
        super().__init__(cellval, shapesval)
        self.iso_plan_val = ""

    def iso_value(self, state_context):
        if self.cellVal == "○" or self.cellVal is not None:
            self.iso_plan_val = "取得予定"
        else:
            if self.shapeval != "":
                self.iso_plan_val = "取得予定"
            else:
                self.iso_plan_val = None

        return self.iso_plan_val


class ISONoCertif(ConcreteISOState):
    def __init__(self, cellval, shapesval):
        super().__init__(cellval, shapesval)
        self.iso_no_certif = ""

    def iso_value(self, state_context):
        if self.cellVal == "○" or self.cellVal is not None:
            self.iso_no_certif = "取得予定なし"
        else:
            if self.shapeval != "":
                self.iso_no_certif = "取得予定なし"
            else:
                self.iso_no_certif = None

        return self.iso_no_certif


