from geoalchemy2 import Geometry
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

class CatastralParcel(declarative_base()):
    __tablename__ = 'catastral_parcels'
    CMIUSCAT = Column(Integer,primary_key=True)
    CMNOMSCAT = Column(String)
    geometry = Column(Geometry('POLYGON'))