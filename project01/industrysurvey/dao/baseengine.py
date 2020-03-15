import sys
import pathlib
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager


class BaseEngine():
    def __init__(self, dbpath) -> None :
        self.sqlpath = "sqlite:///" + dbpath
