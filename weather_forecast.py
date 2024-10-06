import requests
from datetime import datetime

# OpenWeatherMap API key
API_KEY = 'XXXXXXXXXf7XXXXXXX1fXXXXXXX5'    # replace it with your API key

# weather forecast in 3 hour intervals for the next 5 days of a city

def get_weather_forecast(city):
    base_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        forecast_list = data['list']
        
        print(f"Weather Forecast for {city}, {data['city']['country']}:")
        print("-" * 35)
        
        for forecast in forecast_list:
            timestamp = forecast['dt']
            forecast_time = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
            temp = forecast['main']['temp']
            weather_desc = forecast['weather'][0]['description'].capitalize()
            wind_speed = forecast['wind']['speed']
            print(f"Time: {forecast_time}")
            print(f"Temperature: {temp}°C")
            print(f"Weather: {weather_desc}")
            print(f"Wind Speed: {wind_speed} m/s")
            print("-" * 35)
    else:
        print(f"City {city} not found!")

# test with a city name from user
city_name = input("Enter city name for forecast: ")
get_weather_forecast(city_name)
