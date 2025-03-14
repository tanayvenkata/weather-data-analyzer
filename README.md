# Weather Data Analyzer

A Python application that retrieves and displays current weather information using the OpenWeatherMap API.

## Prerequisites

- Python 3.8+
- pip
- Virtual environment support

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/weather-data-analyzer.git
cd weather-data-analyzer
```
Replace `'yourusername'` with your actual username.

### 2. Create and Activate Virtual Environment
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Get OpenWeatherMap API Key
1. Go to [OpenWeatherMap](https://openweathermap.org/)
2. Sign up for a free account
3. Navigate to API Keys section
4. Generate a new API key

### 5. Set API Key
```bash
# On macOS/Linux:
export OPENWEATHERMAP_API_KEY='your_api_key_here'

# On Windows (PowerShell):
$env:OPENWEATHERMAP_API_KEY='your_api_key_here'
```
Replace `'your_api_key_here'` with the actual API key you obtained.

### 6. Run the Application
```bash
python -m weather_app.main
```

## Usage
- Enter city names to get current weather information
- Type 'quit' to exit the application

## Features
- Retrieve current temperature
- Get "feels like" temperature
- View weather description

## Future Improvements
- Add more detailed weather information
- Implement caching
- Create GUI or web interface
