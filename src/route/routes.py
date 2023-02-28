from src.route.models import Route
from src.riskmodel.routecrosses import route_cross_upz

from fastapi import APIRouter

router = APIRouter()

@router.get("/routes/{mode}/")
async def get_endpoint(
        mode: str, source_latitude: float,source_longitude: float,
        target_latitude: float,target_longitude: float, 
        gender: str, hour: str, day: str, month: str 
):
    route = Route (
        mode, source_latitude, source_longitude, 
        target_latitude, target_longitude, 
        gender, hour, day, month
    )
    response = route.get_response()
    routes_shapes = route.get_shape(response.json())
    res = route_cross_upz(routes=routes_shapes, mode=mode, gender=gender, hour=hour)
    for index, value in enumerate(res):
        print(f'🔥 {index} - {value}\n')
        
    return route.get_response().json()
