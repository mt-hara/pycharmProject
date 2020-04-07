from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import relation, relationship
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    address = relationship('Address', order_by='Address.id',
                       uselist=False, backref="users")
    # testtext= relationship("Address", order_by="Address.id",uselist=False)

    def __repr__(self):
        return '<User(%d, %s)>' % (self.id, self.name)


class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer,ForeignKey('users.id'), primary_key=True)
    email = Column(String,nullable=True)
    testtext = Column(String)
    # owner_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return '<Address(%d, %s)>' % (self.id, self.email)


if __name__ == '__main__':
    engine = create_engine('sqlite:///' + "C:\\dev\\sqlite3\\BizSurvey.sqlite3", echo=True)
    Base.metadata.create_all(engine)
    SessionMaker = sessionmaker(bind=engine)
    session = SessionMaker()

    new_user = User(name='foo')
    new_user.address = Address(email='foo@example.jp',testtext="test")

    session.add(new_user)
    session.commit()

    selected_user = session.query(User).first()
    print(selected_user)
    print(selected_user.address)