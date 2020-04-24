from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from sqlalchemy.ext.declarative import declarative_base

DBPATH = "C:\\Dev\\sqlite3\\BizSurvey.sqlite3"
# DBPATH = "G:\\97.ACCESS\\sqlite3db\\BizSurvey.sqlite3"
# DBPATH = "C:\\Dev\\DB\\sqlite3\\BizSurvey.sqlite3"
# DBPATH = "C:\\dev\\sqlite3db\\BizSurvey.sqlite3"

MetaBase = declarative_base()


class BaseEngine():

    def __init__(self) -> None:
        self.sqlpath = "sqlite:///" + DBPATH
        self.engine = create_engine(self.sqlpath, echo=True)


class BaseSession(BaseEngine):
    def __init__(self) -> None:
        super().__init__()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    @contextmanager
    def transaction(self):
        try:
            yield self.session
            self.session.commit()
        except Exception as e:
            print(e)
            self.session.rollback()
        finally:
            self.session.close()
