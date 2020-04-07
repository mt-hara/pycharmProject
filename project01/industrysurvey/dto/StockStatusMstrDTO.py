class AbsStockStatusMasterDTO:
    def __init__(self):
        self.__StockCustomerCd: str = ""
        self.__StockListingStatus: str = ""
        self.__MainStockholder_1: str = ""
        self.__MainStockholder_2: str = ""
        self.__MainStockholder_3: str = ""
        self.__MainStockholder_4: str = ""
        self.__MainStockholder_5: str = ""
        self.__StockRatioSH_1: float = 0
        self.__StockRatioSH_2: float = 0
        self.__StockRatioSH_3: float = 0
        self.__StockRatioSH_4: float = 0
        self.__StockRatioSH_5: float = 0
        
    @property
    def StockCustomerCd(self):
        return self.__StockCustomerCd
    
    @StockCustomerCd.setter
    def StockCustomerCd(self, param):
        self.__StockCustomerCd = param

    @property
    def StockListingStatus(self):
        return self.__StockListingStatus
    
    @StockListingStatus.setter
    def StockListingStatus(self, paramn):
        self.__StockListingStatus = paramn
    
    @property
    def MainStockholder_1(self):
        return self.__MainStockholder_1
    
    @MainStockholder_1.setter
    def MainStockholder_1(self, param):
        self.__MainStockholder_1 = param

    @property
    def MainStockholder_2(self):
        return self.__MainStockholder_2

    @MainStockholder_2.setter
    def MainStockholder_2(self, param):
        self.__MainStockholder_2 = param

    @property
    def MainStockholder_3(self):
        return self.__MainStockholder_3

    @MainStockholder_3.setter
    def MainStockholder_3(self, param):
        self.__MainStockholder_3 = param

    @property
    def MainStockholder_4(self):
        return self.__MainStockholder_4

    @MainStockholder_4.setter
    def MainStockholder_4(self, param):
        self.__MainStockholder_4 = param

    @property
    def MainStockholder_5(self):
        return self.__MainStockholder_5

    @MainStockholder_5.setter
    def MainStockholder_5(self, param):
        self.__MainStockholder_5 = param

    @property
    def StockRatioSH_1(self):
        return self.__StockRatioSH_1
    
    @StockRatioSH_1.setter
    def StockRatioSH_1(self, param):
        self.__StockRatioSH_1 = param

    @property
    def StockRatioSH_2(self):
        return self.__StockRatioSH_2

    @StockRatioSH_2.setter
    def StockRatioSH_2(self, param):
        self.__StockRatioSH_2 = param

    @property
    def StockRatioSH_3(self):
        return self.__StockRatioSH_3

    @StockRatioSH_3.setter
    def StockRatioSH_3(self, param):
        self.__StockRatioSH_3 = param

    @property
    def StockRatioSH_4(self):
        return self.__StockRatioSH_4

    @StockRatioSH_4.setter
    def StockRatioSH_4(self, param):
        self.__StockRatioSH_4 = param

    @property
    def StockRatioSH_5(self):
        return self.__StockRatioSH_5

    @StockRatioSH_5.setter
    def StockRatioSH_5(self, param):
        self.__StockRatioSH_5 = param