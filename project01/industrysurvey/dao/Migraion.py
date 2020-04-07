from dao.BaseEngine import BaseEngine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relation, relationship
from dao.CreateTable import AllCustomerMaster, StockStatusMaster,Base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.engine import  create_engine
class Migration():
    def __init__(self):
        self.e = BaseEngine().engine

    def AllCustomerMaster(self):
        Base().metadata.create_all(self.e)




