from geoalchemy2 import Geometry
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String

class Upz(declarative_base()):
    __tablename__ = 'upz'
    CMIUUPLA = Column(String,primary_key=True)
    CMNOMUPLA = Column(String)
    geometry = Column(Geometry('POLYGON'))