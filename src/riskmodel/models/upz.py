from src.database.base import Base

from geoalchemy2 import Geometry
from sqlalchemy import Column, String

class Upz(Base):
    __tablename__ = 'upz'
    CMIUUPLA = Column(String,primary_key=True)
    CMNOMUPLA = Column(String)
    geometry = Column(Geometry('POLYGON'))
