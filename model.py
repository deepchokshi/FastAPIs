from sqlalchemy import Column, Integer, String, Boolean, Numeric, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, index=True)
    title = Column(String(15), nullable=False)
    author = Column(String(15), nullable=False)
    category = Column(String(15), nullable=False)