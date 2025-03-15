import os
from weather_app.data_collector import WeatherDataCollector


def main():
    # Retrieve API key from environment variable
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")

    if not api_key:
        print("Error: Please set the OPENWEATHERMAP_API_KEY environment variable.")
        return

    # Create an instance of WeatherDataCollector
    weather_collector = WeatherDataCollector(api_key)

    # Get user input for city
    while True:
        city = input("Enter a city name (or 'quit' to exit): ").strip()

        if city.lower() == "quit":
            break

        # Fetch weather data
        try:
            weather_data = weather_collector.get_current_weather(city)

            if weather_data:
                # Extract and display temperature data
                temp_info = weather_collector.extract_temperature_data(weather_data)

                print("\n--- Weather Information ---")
                print(f"City: {city.title()}")
                print(f"Current Temperature: {temp_info['current_temperature']}°F")
                print(f"Feels Like: {temp_info['feels_like_temperature']}°F")
                print(f"Description: {temp_info['description'].capitalize()}")
                print("------------------------\n")
            else:
                print(
                    f"Could not retrieve weather data for {city}. Please check the city name."
                )

        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
