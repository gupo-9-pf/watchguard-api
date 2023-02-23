from shapely import wkt
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, func
from base.catastralparcel import CatastralParcel
from base.upz import Upz
from models.route import Route
from shapely import LineString

engine = create_engine('postgresql://postgres:1919@localhost:5432/postgis')
Session = sessionmaker(bind=engine)
session = Session()


def route_cross_cat(routes: list[LineString]):
    results = []
    for route in routes:
        str_wkt = wkt.dumps(route)
        results.append(session.query(CatastralParcel.CMNOMSCAT).filter(func.ST_Crosses(CatastralParcel.geometry,func.ST_SetSRID(func.ST_GeomFromText(str_wkt), 4326))).all())
    return results

def route_cross_upz(routes: list[LineString], mode, gender, hour):
    results = []
    for route in routes:
        str_wkt = wkt.dumps(route)
        if mode == 'car' and gender == 'male' and hour == 'morning':
            results.append(session.query(Upz.CMIUUPLA,Upz.CMNOMUPLA).filter(func.ST_Crosses(Upz.geometry,func.ST_SetSRID(func.ST_GeomFromText(str_wkt), 4326))).all())
    return results