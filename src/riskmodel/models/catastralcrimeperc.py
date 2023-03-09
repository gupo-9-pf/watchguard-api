from src.database.base import Base

from sqlalchemy import Column, Float, String

class CatastralCrimePercentages(Base):
    __tablename__ = 'order_crime_catastral_per'
    index = Column(String, primary_key=True)
    car = Column(Float)
    motorbike = Column(Float)
    bike = Column(Float)
    foot = Column(Float)
