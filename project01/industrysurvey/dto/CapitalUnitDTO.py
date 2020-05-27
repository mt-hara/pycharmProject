import unicodedata


class AbstractCapuitalUnit():
    def __init__(self):
        self.__xlCustomerCd: str = ""  # H3
        self.__xlCustomerName: str = ""  # H5
        self.__xlCustomerCapital: float = 0  # H18
        self.__xlCapitalUnit: str = ""  # Q18

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
    def xlCustomerCapital(self):
        return self.__xlCustomerCapital

    @xlCustomerCapital.setter
    def xlCustomerCapital(self, param: float):
        self.__xlCustomerCapital = param

    @property
    def xlCapitalUnit(self):
        return self.__xlCapitalUnit

    @xlCapitalUnit.setter
    def xlCapitalUnit(self, param: str):
        self.__xlCapitalUnit = param


class CaputalUnit(AbstractCapuitalUnit):
    def __init__(self, ws):
        super(CaputalUnit, self).__init__()
        self.ws = ws
        self.xlCustomerCd: str = self.cells("H3", str) # H3
        self.xlCustomerName: str = self.cells("H5", str) # H5
        self.xlCapitalUnit: str = self.cells("Q18", str) # Q18
        self.xlCustomerCapital: float = self.cells_capital("H18")

    def __get_cells(self, range_value: str):
        return self.ws.range(range_value).value

    def cells_capital(self, range_value):
        param = self.__get_cells(range_value)

        if param == None:
            return None
        elif type(param) == int or type(param) == float:
            if self.xlCapitalUnit == "千円":
                val = float(param)/1000
                return val
            elif self.xlCapitalUnit == "百万円":
                return float(param)
            else:
                return 9999999999999999999999

    def cells(self, range_value: str, datatype):
        param = self.__get_cells(range_value)
        # Cellのデータ型とDTOのデータ型の整合性を取る
        if param == None:
            return None

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
        # 数値以外の場合でDTOLのデータ型がSTRの以外の場合はNoneを代入
        else:
            if datatype == str:
                han_param = self.str_zen_han(param)
                s_param = self.strip_string(han_param)
                return str(s_param)
            else:
                return None

    def str_zen_han(self, param):
        tmp = unicodedata.normalize("NFKC", param)
        return str(tmp)

    def strip_string(self, param: str):
        tmp = param.strip()
        return str(tmp)
