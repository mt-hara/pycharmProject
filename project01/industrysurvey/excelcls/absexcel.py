import xlwings as xlw
from  abc import ABCMeta
from abc import  abstractmethod


class Singleton():
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class AbstractExcelApp(Singleton,metaclass=ABCMeta):
    """
    ExcelApplication 基底クラス
    Singletonクラスを継承
    """

    def __init__(self):
        self.__app = xlw.App(visible=True)
        self.__app.calculation = "manual"
        self.__app.display_alerts = False
        self.instwb = None

    @property
    def app(self):
        return self.__app

    @app.setter
    def app(self, application):
        self.__app = application

    def get_wb(self, *args):
        pass

    def close_app(self):
        self.app.quit()


class AbstractExcelWorkBook(metaclass=ABCMeta):
    def __init__(self):
        self.__exlwb = None
        self.__exlws = None

    @property
    def exlwb(self):
        return self.__exlwb

    @exlwb.setter
    def exlwb(self, wb):
        self.__exlwb = wb

    @property
    def exlws(self):
        return self.__exlws

    @exlws.setter
    def exlws(self, ws):
        self.__exlws = ws

    def set_wb(self):
        pass

    @abstractmethod
    def open_wb(self, *args):
        pass

    @abstractmethod
    def close_wb(self):
        pass

