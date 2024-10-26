import requests
from ..config.config import API_KEY, CITIES
from datetime import datetime

# Constant for N/A
NA = 'N/A'

# fetch_weather_data
def fetch_weather_data(city):
    """Fetch current weather data for a given city."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        timestamp = datetime.fromtimestamp(data['dt']).strftime('%Y-%m-%d %H:%M:%S')
        return {
            'city': city,
            'temp': data['main'].get('temp', NA),
            'feels_like': data['main'].get('feels_like', NA),
            'condition': data['weather'][0].get('main', NA),
            'main_condition': data['weather'][0].get('description', NA),
            'humidity': data['main'].get('humidity', NA),
            'wind_speed': data['wind'].get('speed', NA),
            'min_temp': data['main'].get('temp_min', NA),
            'max_temp': data['main'].get('temp_max', NA),
            'timestamp': timestamp
        }
    else:
        print(f"Error fetching data for {city}: {response.status_code}")
        return None
    
# fetch_forecast_data
def fetch_forecast_data(city):
    """Fetch the next 5 days of weather forecast for a given city."""
    # Use the 5-day forecast endpoint
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        forecast_list = []

        # Extract the forecast for the next 5 days
        for entry in data['list']:
            date = datetime.fromtimestamp(entry['dt']).strftime('%Y-%m-%d')
            temp = entry['main'].get('temp', NA)
            condition = entry['weather'][0].get('main', NA)

            # Store only the necessary forecast entry
            forecast_list.append({
                'date': date,
                'temp': round(float(temp), 2) if temp != NA else NA,  # Round temperature to two decimal places
                'condition': condition
            })

        # We only want the next 5 unique dates from the forecast
        unique_dates = sorted(set(f['date'] for f in forecast_list))
        next_5_days_forecast = []

        for date in unique_dates[:5]:  # Get only the next 5 unique dates
            # Find the first matching forecast for the date
            for forecast in forecast_list:
                if forecast['date'] == date:
                    next_5_days_forecast.append({
                        'date': date,
                        'temp': forecast['temp'],
                        'condition': forecast['condition']
                    })
                    break  # Only take the first entry for the date

        return next_5_days_forecast
    else:
        print(f"Error fetching forecast data for {city}: {response.status_code}")
        return None

# fetch_all_weather_data
def fetch_all_weather_data():
    """Fetch weather data for all defined cities."""
    weather_data = []
    for city in CITIES:
        data = fetch_weather_data(city)
        if data:
            weather_data.append(data)
    return weather_data
