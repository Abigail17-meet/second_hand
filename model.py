from sqlalchemy import Column,Integer,String, DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, func
from passlib.apps import custom_app_context as pwd_context
from datetime import datetime

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    address = Column(String(255))
    email = Column(String(255), unique=True)
    password_hash = Column(String(255))
    items = relationship("Item", back_populates="customer")
    comments = relationship("Comment", back_populates="customer")

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    description = Column(String(255))
    picture = Column(String(255))
    price = Column(String(255))
    location = Column(String(255))
    customer = relationship("Customer", back_populates="items")
    customer_id = Column(Integer, ForeignKey('customer.id'))
    comments = relationship("Comment", back_populates="item")

class Comment(Base):
    __tablename__ = 'comment'
    #now = datetime.now()
    id = Column(Integer, primary_key=True)
    text = Column(String(255))
    customer = relationship("Customer", back_populates="comments")
    item = relationship("Item", back_populates="comments")
    customer_id = Column(Integer, ForeignKey('customer.id'))
    item_id = Column(Integer, ForeignKey('item.id'))



engine = create_engine('sqlite:///Second_hand.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine, autoflush=False)

session = DBSession()

