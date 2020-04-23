from dao.BaseEngine import BaseEngine, MetaBase
from dao.TableModel.AllCustomerMaster import AllCustomerMaster

class TableMigrationAll(BaseEngine):
    def __init__(self):
        super().__init__()
        try:
            MetaBase().metadata.create_all(self.engine)
        except Exception as e:
            print(e)

class TableDeleteAllCustomer(BaseEngine):
    def __init__(self):
        super().__init__()
        try:
            MetaBase.metadata.drop_all(bind=self.engine)
        except Exception as e:
            print(e)

if __name__ =="__main__":
    TableDeleteAllCustomer()
    TableMigrationAll()
