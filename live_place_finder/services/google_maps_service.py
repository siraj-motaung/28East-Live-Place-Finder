import requests


class GoogleMapsService:
    BASE_URL = "https://maps.googleapis.com/maps/api/"

    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("Google API key is missing")
        self.api_key = api_key

    def geocode(self, address: str) -> dict:
        url = f"{GoogleMapsService.BASE_URL}geocode/json"
        response = requests.get(url, params={
            "address": address,
            "key": self.api_key
        })
        return response.json()

    def nearby_search(self, lat: float, lng: float, place_type: str) -> dict:
        url = f"{GoogleMapsService.BASE_URL}place/nearbysearch/json"
        response = requests.get(url, params={
            "location": f"{lat},{lng}",
            "radius": 2000,
            "type": place_type,
            "key": self.api_key
        })
        return response.json()
