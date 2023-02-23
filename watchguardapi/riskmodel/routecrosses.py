from sqlalchemy import create_engine, func
from base.catastralparcel import CatastralParcel
from base.upz import Upz
from models.route import Route
from base.upzcrimeper import UpzCrimePercentages

from shapely import wkt
from sqlalchemy.sql.expression import select
from sqlalchemy.orm import sessionmaker
from geoalchemy2 import functions

engine = create_engine('postgresql://postgres:melo@localhost:5432/postgres')
Session = sessionmaker(bind=engine)
session = Session()


def route_cross_cat(routes: list):
    results = []
    for route in routes:
        str_wkt = wkt.dumps(route)
        results.append(
            session
            .query(CatastralParcel.CMNOMSCAT)
            .filter(func.ST_Crosses(CatastralParcel.geometry,func.ST_SetSRID(func.ST_GeomFromText(str_wkt), 4326)))
            .all()
        )
    return results

def route_cross_upz(routes: list, mode, gender, hour):
    results = []
    for route in routes:
        str_wkt = wkt.dumps(route)
        if mode == 'car' and gender == 'male' and hour == 'morning':
            # results.append(
            #     session
            #     .query(Upz.CMIUUPLA,Upz.CMNOMUPLA)
            #     .filter(func.ST_Crosses(Upz.geometry,func.ST_SetSRID(func.ST_GeomFromText(str_wkt), 4326)))
            #     .all()
            # )
            results.append(
                session.execute(
                    select([Upz.CMNOMUPLA, UpzCrimePercentages.morning_car_m])
                    .select_from(session.query(Upz, UpzCrimePercentages).join(UpzCrimePercentages, Upz.CMIUUPLA == UpzCrimePercentages.index))
                    .where(functions.ST_Crosses(Upz.geometry,functions.ST_SetSRID(func.ST_GeomFromText(str_wkt), 4326)))
                )
                .all()
            )
    return results
