from dao.BaseEngine import BaseSession
from abc import ABCMeta, abstractmethod

class Report():
    def __init__(self, title,types):
        self.title = title
        self.typys = types


    def printer(self):
        self.typys.execute(self.title)

class IExecute(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, title):
        pass