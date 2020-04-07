from dao.BaseEngine import BaseEngine
from dao.Models import CustomerMaster,StockStatusMaster,Base

class Migration():
    def __init__(self):
        self.e = BaseEngine().engine

    def CustomerMaster(self):
        Base().metadata.create_all(self.e)
