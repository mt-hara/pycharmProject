from dao.BaseEngine import BaseSession, MetaBase
from abc import ABCMeta, abstractmethod
from typing import Dict, Any
# from dao.tablemodel.CustomerMaster import CustomerMaster
# from dao.tablemodel.StockStatusMaster import StockStatusMaster
from dao.crud.UpdateData import Update
from dao.crud.InsertData import Insert


class RunQuery():
    def __init__(self, xldto, querytype):
        self.xldto = xldto
        self.querytype = querytype

    def execute(self):
        self.querytype.execute(self.xldto)


# class Excecute():
#     @abstractmethod
#     def execute(self, xldto):
#         pass

class ExecuteNonQery():
    def __init__(self):
        self.pattern = chose_pattern(0)
        query = RunQuery('', self.pattern)
        query.execute()


def chose_pattern(param):
    base = BaseSession()
    if param == 0:
        return Insert(param)
    else:
        return Update(param)




if __name__ == "__main__":
    ExecuteNonQery()
