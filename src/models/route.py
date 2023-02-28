import requests
from dataclasses import dataclass
from requests import Response
from shapely.geometry import LineString

@dataclass
class Route:
    mode: str
    source_latitude: float
    source_longitude: float
    target_latitude: float
    target_longitude: float
    gender: str
    hour: str
    day: str
    month: str

    def get_shape(self, response: dict) -> LineString:
        return [LineString(item['geometry']['coordinates'])
                for item in response.get('routes')]

    def get_response(self) -> Response:
        url: str = f'https://routing.openstreetmap.de/routed-{self.mode}/route/v1/driving/{self.source_longitude},{self.source_latitude};{self.target_longitude},{self.target_latitude}?alternatives=true&overview=full&steps=true&geometries=geojson'
        return requests.get(url=url)
