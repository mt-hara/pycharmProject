from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager


class BaseEngine():
    def __init__(self, dbpath) -> None :
        self.sqlpath = "sqlite:///" + dbpath
        self.engine = create_engine(self.sqlpath, echo=True)

class BaseSession(BaseEngine):
    def __init__(self, dbpath) -> None:
        super().__init__(dbpath)
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