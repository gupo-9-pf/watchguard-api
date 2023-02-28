from src.database.base import Base

from geoalchemy2 import Geometry
from sqlalchemy import Column, Float, String, Integer

class CatastralParcel(Base):
    __tablename__ = 'catastral_parcels'
    CMIUSCAT = Column(Integer, primary_key=True)
    CMNOMSCAT = Column(String)
    geometry = Column(Geometry('POLYGON'))
