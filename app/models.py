from sqlalchemy import (Column, Integer, String, Boolean,
                        ForeignKey, UniqueConstraint)
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session, relationship, backref
from sqlalchemy import create_engine
from config import SQLALCHEMY_DATABASE_URI


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    password = Column(String)

    def __repr__(self):
        return '<User:"{}">'.format(self.name)


class Redirection(Base):
    __tablename__ = 'redirections'
    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship('User', backref=backref('redirections'))
    redirect_hash = Column(String, unique=True)
    redirect_value = Column(String)
    active = Column(Boolean, default=True)

    def __repr__(self):
        return '<Redirection: "{}">'.format(self.redirect_value)


engine = create_engine(SQLALCHEMY_DATABASE_URI, encoding='utf8', echo=False)
DBSession = scoped_session(sessionmaker(bind=engine))
Base.metadata.bind = engine
Base.metadata.create_all(engine)
