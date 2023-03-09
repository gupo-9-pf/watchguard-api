from src.models.route import Route
from src.riskmodel.routecrosses import route_cross_upz, route_cross_cat

from fastapi import APIRouter
from statistics import mean

router = APIRouter()

@router.get("/routes/{mode}/")
async def get_routes(
        mode: str, source_latitude: float,source_longitude: float,
        target_latitude: float,target_longitude: float, 
        gender: str, hour: str, day: str, month: str 
):
    route = Route (
        mode, source_latitude, source_longitude, 
        target_latitude, target_longitude, 
        gender, hour, day, month
    )
    
    response_json = route.get_response().json()
    routes_shapes = route.get_shape(response_json)
    res_upz = route_cross_upz(routes=routes_shapes, mode=mode, gender=gender, hour=hour)
    res_cat = route_cross_cat(routes=routes_shapes, mode=mode)
    
    for value in range(len(res_cat)):
        risk_upz_route = mean(map(lambda x: x[2],  res_upz[value]))
        risk_cat_route = mean(map(lambda x: x[2],  res_cat[value]))
        risk_route = (0.7 * risk_cat_route) + (0.3 * risk_upz_route)
        response_json['routes'][value]['risk'] = risk_route
    
    return response_json
