from dao.BaseEngine import BaseSession, MetaBase
from dao.tablemodel.CustomerMaster import CustomerMaster
from dao.tablemodel.BizConditionsMaster import BizConditionsMaster
from dao.tablemodel.StockStatusMaster import StockStatusMaster
from dao.tablemodel.MainSupplierMaster import MainSupplierMaster
from dao.tablemodel.MainProductMaster import MainProductMaster

class TableMigration(BaseSession):
    def __init__(self):
        super().__init__()
        try:
            MetaBase().metadata.create_all(self.engine)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    TableMigration()
