from fastapi import FastAPI
from route import Route

app = FastAPI()

@app.get("/watchguard/api/requestroute/{mode}/{source_latitude}/{source_longitude}/{target_latitude}/{target_longitude}/{gender}/{hour}/{day}/{month}")
async def get_endpoint(mode: str, source_latitude: float,source_longitude: float,
                       target_latitude: float,target_longitude: float, 
                       gender: str, hour: str, day: str, month: str ):
    route = Route (mode, source_latitude, source_longitude, 
                   target_latitude, target_longitude, 
                   gender, hour, day, month)
    return route.get_response().json()
