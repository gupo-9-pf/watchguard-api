from src.database.session import session
from src.riskmodel.models.upz import Upz
from src.riskmodel.models.catastralparcel import CatastralParcel
from src.riskmodel.models.upzcrimeperc import UpzCrimePercentages
from src.riskmodel.models.catastralcrimeperc import CatastralCrimePercentages

from shapely import wkt
from shapely.geometry import LineString
from sqlalchemy import func


def route_cross_cat(routes: list, mode: str):
    results = []
    for route in routes:
        str_wkt = wkt.dumps(route)
        results.append(
            session
            .query(CatastralParcel.CMIUSCAT, CatastralParcel.CMNOMSCAT,  getattr(CatastralCrimePercentages, mode))
            .join(CatastralParcel, CatastralParcel.CMIUSCAT == CatastralCrimePercentages.index)
            .filter(func.ST_Crosses(CatastralParcel.geometry, func.ST_SetSRID(func.ST_GeomFromText(str_wkt), 4326)))
            .all()
        )
    return results


def route_cross_upz(routes: list[LineString], mode: str, gender: str, hour: str):
    results = []
    for route in routes:
        str_wkt = wkt.dumps(route)
        column_name = f'{hour}_{mode}_{gender}'
        query_result = (
            session
            .query(Upz.CMIUUPLA, Upz.CMNOMUPLA, getattr(UpzCrimePercentages, column_name))
            .join(Upz, Upz.CMIUUPLA == UpzCrimePercentages.index)
            .filter(func.ST_Crosses(Upz.geometry, func.ST_SetSRID(func.ST_GeomFromText(str_wkt), 4326)))
            .all()
        )
        results.append(query_result)       
    return results

