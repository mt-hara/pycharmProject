import sys
import pathlib
from dao.baseengine import BaseSession
from dao.models import CustomerData


class Customers(BaseSession):
    def __init__(self, dbpath):
        super().__init__(dbpath)

    def select(self):
        with self.transaction() as session:
            for i in self.session.query(CustomerData):
                print("id = {} : name = {}".format(i.customerCd, i.customerName))

    def like_select(self, keyword):
        with self.transaction() as session:
            for i in self.session.query(CustomerData).filter(CustomerData.customerName.like('%' +
                                                                                            keyword + '%')):
                return i.customerCd

if __name__ == "__main__":
    sqlite_patrh = "C:\\dev\\sqlite3\\BizSurvey.sqlite3"
    cli = Customers(sqlite_patrh)
    # cli.select()
    strfld = cli.like_select("シーシーエス")
    print(str(strfld))