from fastapi import FastAPI
from models.route import Route
from riskmodel.routecrosses import route_cross_cat, route_cross_upz

app = FastAPI()

@app.get("/watchguard/api/requestroute/{mode}/{source_latitude}/{source_longitude}/{target_latitude}/{target_longitude}/{gender}/{hour}/{day}/{month}")
async def get_endpoint(mode: str, source_latitude: float,source_longitude: float,
                       target_latitude: float,target_longitude: float, 
                       gender: str, hour: str, day: str, month: str ):
    route = Route (mode, source_latitude, source_longitude, 
                   target_latitude, target_longitude, 
                   gender, hour, day, month)
    response = route.get_response()
    #print(route_cross_cat(route.get_shape(response.json())))
    print(route_cross_upz(route.get_shape(response.json()), mode, gender, hour))
    return route.get_response().json()
