from dao.BaseEngine import BaseEngine, BaseSession, MetaBase
from dao.tablemodel.CustomerMaster import CustomerMaster
from dao.tablemodel.BizConditionsMaster import BizConditionsMaster
from dao.tablemodel.StockStatusMaster import StockStatusMaster
from dao.tablemodel.MainProductMaster import MainProductMaster
from dao.tablemodel.MainSupplierMaster import MainSupplierMaster


class TableMigration(BaseSession):
    """
    importしたモデルクラスのテーブルを生成する。
    """
    def __init__(self):
        super().__init__()
        try:
            MetaBase().metadata.create_all(self.engine)
        except Exception as e:
            print(e)
        else:
            print("Finish")


if __name__ == "__main__":
    TableMigration()