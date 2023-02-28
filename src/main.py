from src.routes import route

from fastapi import FastAPI

app = FastAPI()

app.include_router(route.router)
