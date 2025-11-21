# create a student model
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    mat_number = Column(String, unique=True)
    major = Column(String)
    age = Column(Integer)
    email = Column(String(255), unique=True)
    phone_number = Column(String(20), unique=True)
    address = Column(String(500))
