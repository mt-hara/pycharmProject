from dao.TableModel.CustomerMaster import CustomerMaster
from dao.BaseEngine import BaseSession
from dao.tabledao.ImpCRUD import IExecute

class Instert(BaseSession, IExecute):
    def execute(self, title):
        print("insert:{}".format(title))

class Update(BaseSession, IExecute):
    def execute(self, title):
        print("Update:{}".format(title))