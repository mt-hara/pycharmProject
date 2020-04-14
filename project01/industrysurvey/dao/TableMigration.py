from dao.BaseEngine import BaseSession, MetaBase
from dao.TableModel.CustomerMaster import CustomerMasterMigration
from dao.TableModel.BizConditionsMaster import BizConditionsMaster
# from dao.TableModel.StockStatusMaster import StockStatusMaster
# from dao.TableModel.MainSupplierMaster import MainSupplierMaster
# from dao.TableModel.MainProductMaster import MainProductMaster

class TableMigration(BaseSession):
    def __init__(self):
        super().__init__()
        try:
            MetaBase().metadata.create_all(self.engine)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    TableMigration()
