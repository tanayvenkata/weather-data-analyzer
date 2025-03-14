import os
import unittest
from weather_app.data_collector import WeatherDataCollector

class TestWeatherDataCollector(unittest.TestCase):
    def setUp(self):
        # Get API key from environment variable
        self.api_key = os.getenv('OPENWEATHERMAP_API_KEY')
        self.collector = WeatherDataCollector(self.api_key)

    def test_get_current_weather(self):
        # Test fetching weather for a known city
        weather_data = self.collector.get_current_weather('London')
        
        # Check that we get a valid response
        self.assertIsNotNone(weather_data)
        self.assertIn('main', weather_data)
        self.assertIn('temp', weather_data['main'])

    def test_extract_temperature_data(self):
        # Simulate weather data
        mock_weather_data = {
            "main": {
                "temp": 75.5,
                "feels_like": 73.2
            },
            "weather": [
                {
                    "description": "partly cloudy"
                }
            ]
        }
        
        # Extract temperature data
        temp_info = self.collector.extract_temperature_data(mock_weather_data)
        
        # Check extracted data
        self.assertEqual(temp_info['current_temperature'], 75.5)
        self.assertEqual(temp_info['feels_like_temperature'], 73.2)
        self.assertEqual(temp_info['description'], 'partly cloudy')

    def test_invalid_city(self):
        # Test with an invalid city name
        weather_data = self.collector.get_current_weather('InvalidCityName123')
        
        # Check that we get None for an invalid city
        self.assertIsNone(weather_data)

if __name__ == '__main__':
    unittest.main()