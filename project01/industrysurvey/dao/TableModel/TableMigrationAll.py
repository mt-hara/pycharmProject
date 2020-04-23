from dao.BaseEngine import BaseEngine, MetaBase
from dao.TableModel.AllCustomerMaster import AllCustomerMaster

class TableMigrationAll(BaseEngine):
    def __init__(self):
        super().__init__()
