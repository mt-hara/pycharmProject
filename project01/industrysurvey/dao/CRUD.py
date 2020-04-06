import sys
import pathlib
from os.path import join

from dao.BaseEngine import BaseSession
from dao.Models import CustomerData
from dao.Models import AllCustomerMaster


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

    def update(self, keyword, param):
        with self.transaction() as session:
            i = self.session.query(CustomerData).filter(CustomerData.customerCd ==
                                                        keyword).first()
            print(":{}:{}:{}".format(i.customerCd, i.customerName, i.fld1))
            i.fld1 = param
            print(":{}:{}:{}".format(i.customerCd, i.customerName, i.fld1))


class AllCustomer(BaseSession):
    def __init__(self, dbpath):
        super().__init__(dbpath)

    def insert(self, cd, name):
        with self.transaction() as session:
            customer = AllCustomerMaster()
            customer.CustomerCd = cd
            customer.CustomerName = name
            self.session.add(customer)
            # AllCustomerMaster().insert().values(CustomerCd = cd)

            # self.session.add(i)


if __name__ == "__main__":
    # sqlite_patrh = "G:\\97.ACCESS\\sqlite3db\\BizSurvey.sqlite3"
    # "sqlite:///"
    # "G:\\97.ACCESS\\sqlite3db\\BizSurvey.sqlite3"
    # sqlpath = "sqlite:///" + "C:\\dev\\sqlite3\\BizSurvey.sqlite3"
    sqlite_patrh = "C:\\dev\\sqlite3\\BizSurvey.sqlite3"
    # "C:\dev\sqlite3\BizSurvey.sqlite3"

    cli = AllCustomer(sqlite_patrh)
    cli.insert("12334", "test")
    # cli.select()
    # strfld = cli.like_select("シーシーエス")
    # print(str(strfld))
    # cli.update("001002",None)
