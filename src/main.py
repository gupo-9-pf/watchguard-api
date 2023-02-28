from src.route import routes as route_routes

from fastapi import FastAPI

app = FastAPI()

app.include_router(route_routes.router)
