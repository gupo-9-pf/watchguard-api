from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Float, String

class UpzCrimePercentages(declarative_base()):
    __tablename__ = 'order_crime_upz_perc'
    index = Column(String,primary_key=True)
    morning_bicy_m = Column(Float)
    morning_bicy_f = Column(Float)
    aftern_bicy_m= Column(Float)
    aftern_bicy_f= Column(Float)
    night_bicy_m= Column(Float)
    night_bicy_f= Column(Float)
    morning_walk_m= Column(Float)
    morning_walk_f= Column(Float)
    aftern_walk_m= Column(Float)
    aftern_walk_f= Column(Float)
    night_walk_m= Column(Float)
    night_walk_f= Column(Float)
    morning_car_m= Column(Float)
    morning_car_f= Column(Float)
    aftern_car_m= Column(Float)
    aftern_car_f= Column(Float)
    night_car_m= Column(Float)
    night_car_f= Column(Float)
    type_1_events= Column(Float)
    type_2_events= Column(Float)
    type_3_events= Column(Float)

