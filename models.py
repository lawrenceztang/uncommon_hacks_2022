from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
# from sqlalchemy.ext.declarative import declarative_base
from database import Base, db_session
from sqlalchemy.orm import relationship

# Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    # query = db_session.query_property()

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

    # queue = relationship("Queue", back_populates="user", useList=False)

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password
    
    def __repr__(self):
        return f'User {self.id}'
        
class Queue(Base):
    __tablename__ = 'queue'

    id = Column(Integer, primary_key=True)
    video = Column(String)

    # user_id = Column(Integer, ForeignKey('user.id'))
    # user = relationship("User", back_populates="queue")

    creation_time = Column(DateTime, default=func.now())

    def __init__(self, id=None, video=None):
        self.id = id
        self.video = video

    def __repr__(self):
        return f'Queue {self.id}'