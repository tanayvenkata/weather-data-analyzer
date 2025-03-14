import requests
from datetime import datetime

class WeatherDataCollector:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
        
    def get_current_weather(self, city):
        params = {
            "q": city,            # City name
            "appid": self.api_key,  # Authentication key
            "units": "imperial"     # Temperature
        }
        
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()

            return response.json()
        
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {e}")

            return None
        
    def extract_temperature_data(self, weather_data):
        current_temp = weather_data["main"]["temp"]
        feels_like_temp = weather_data["main"]["feels_like"]
        description = weather_data["weather"][0]["description"]

        return {
            "current_temperature": current_temp,
            "feels_like_temperature": feels_like_temp,
            "description": description
        }

