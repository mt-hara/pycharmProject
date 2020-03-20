# from typing import *
import xlwings as xlw
from abc import ABCMeta
from abc import abstractmethod


# Applicationの重複起動防止の為Singletonパターンを適用
class Singleton():
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class AbstractExcelApp(Singleton):
    """
    ExcelApplication 基底クラス
    Singletonクラスを継承
    """
    def __init__(self):
        self.__app = xlw.App(visible=True)
        self.__app.calculation = "manual"
        self.__app.display_alerts = False

    @property
    def app(self):
        return self.__app

    @app.setter
    def app(self, application):
        self.__app = application


class AbstaractWorkBook(metaclass=ABCMeta):
    """
    Excel Workbook基底クラス
    """
    def __init__(self):
        self.__xlapp = AbstractExcelApp().app
        self.__xlwb: object = None
        self.__xlws: object = None

    @property
    def xlapp(self):
        return self.__xlapp

    @xlapp.setter
    def xlapp(self, params):
        self.__xlapp = params

    @property
    def xlwb(self):
        return self.__xlwb

    @xlwb.setter
    def xlwb(self,instws):
        self.__xlwb = instws

    @property
    def xlws(self):
        return  self.__xlws

    @xlws.setter
    def xlws(self, instws):
        self.__xlws = instws

    def close_app(self):
        self.xlapp.quit()

    @abstractmethod
    def open_wb(self, *args):
        pass

    @abstractmethod
    def close_wb(self):
        pass

    @abstractmethod
    def select_sheet(self):
        pass

class AbstractGetSheetData():
    pass