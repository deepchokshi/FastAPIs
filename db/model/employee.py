from sqlalchemy import Column, Integer, Numeric, Boolean, String, ForeignKey
from sqlalchemy.orm import declarative_base
from enum import Enum

Base = declarative_base()

class JobTitle(Enum):
    ceo = "CEO"
    team_lead = "Team Lead"
    intern = "Intern"

class Employee(Base):
    id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True)
    first_name = Column(String(20), nullable=False)
    middle_name = Column(String(20))
    last_name = Column(String(20), nullable=False)
    job_title = Column(String(20), nullable=False)

