from dao.BaseEngine import BaseEngine, MetaBase
from dao.TableModel.CustomerMaster import CustomerMaster
from dao.TableModel.BizConditionsMaster import BizConditionsMaster
from dao.TableModel.StockStatusMaster import StockStatusMaster
from dao.TableModel.MainSupplierMaster import MainSupplierMaster
from dao.TableModel.MainProductMaster import MainProductMaster

class TableMigration(BaseEngine):
    def __init__(self):
        super().__init__()
        try:
            MetaBase().metadata.create_all(self.engine)
        except Exception as e:
            print(e)

class TableDelete(BaseEngine):
    def __init__(self):
        super().__init__()
        try:
            MetaBase.metadata.drop_all(bind=self.engine)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    TableDelete()
    # TableMigration()
    # TableDelete()
