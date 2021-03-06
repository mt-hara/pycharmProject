import xlwings as xlw
from abc import ABCMeta

def singleton(class_):
    class class_w(class_):
        _instance = None
        def __new__(class_, *args, **kwargs):
            if class_w._instance is None:
                class_w._instance = super(class_w, class_).__new__(class_, *args, **kwargs)
                class_w._instance._sealed = False
            return class_w._instance
        def __init__(self, *args, **kwargs):
            if self._sealed:
                return
            super(class_w, self).__init__(*args, **kwargs)
            self._sealed = True
    class_w.__name__ = class_.__name__
    return class_w

@singleton
class AbstractExcelApp(metaclass=ABCMeta):
    """
    ExcelApplication 基底クラス
    Singletonクラスを継承
    """

    def __init__(self):
        self.__app = None
        self.__app = xlw.App(visible=False)
        self.__app.calculation = "manual"
        self.__app.display_alerts = False

    @property
    def app(self):
        return self.__app

    @app.setter
    def app(self, application):
        self.__app = application

    def close_App(self):
        self.app.kill()


class AbstractExcelWorkBook(metaclass=ABCMeta):
    def __init__(self):
        self.__xlwb = None
        self.__xlws = None

    @property
    def xlwb(self):
        return self.__xlwb

    @xlwb.setter
    def xlwb(self, obj):
        self.__xlwb = obj

    @property
    def xlws(self):
        return self.__xlws

    @xlws.setter
    def xlws(self, obj):
        self.__xlws = obj

    # @abstractmethod
    def open_wb(self, *args):
        pass

    # @abstractmethod
    def close_workbook(self):
        pass
