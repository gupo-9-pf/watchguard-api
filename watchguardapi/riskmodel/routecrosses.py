from shapely import wkt
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, func
from base.catastralparcel import CatastralParcel
from models.route import Route
from shapely import LineString

engine = create_engine('postgresql://postgres:1919@localhost:5432/postgis')
Session = sessionmaker(bind=engine)
session = Session()

def route_cross(routes: list[LineString]):
    results = []
    for route in routes:
        str_wkt = wkt.dumps(route)
        results.append(session.query(CatastralParcel.CMNOMSCAT).filter(func.ST_Crosses(CatastralParcel.geometry,func.ST_SetSRID(func.ST_GeomFromText(str_wkt), 4326))).all())
    return results