from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

DBPATH = "C:\\Dev\\DB\\sqlite3\\BizSurvey.sqlite3"
# "G:\\97.ACCESS\\sqlite3db\\BizSurvey.sqlite3"
# "C:\\Dev\\DB\\sqlite3\\BizSurvey.sqlite3"
# "C:\\dev\\sqlite3\\BizSurvey.sqlite3"

class BaseEngine():

    def __init__(self) -> None :
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
        except:
            self.session.rollback()
        finally:
            self.session.close()
