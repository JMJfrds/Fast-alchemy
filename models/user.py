from database import Base
from sqlalchemy import Column, String, Integer


class User(Base):
    __tablename__ = "user"


    id = Column(Integer, primary_key  = True, nullable = False)
    username = Column(String, unique = True, nullable = False)
    password = Column(String, nullable = False)
