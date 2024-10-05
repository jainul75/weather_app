import requests     # for sending HTTP requests
from datetime import datetime, timedelta

# OpenWeatherMap API key
API_KEY = '2XXXXXX5XXXXX7XXXX'    # put your API key here

# create a function
def get_weather(city):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']     # fetching temperature related data
        wind = data['wind']
        weather_desc = data['weather'][0]['description']
        timezone_offset = data['timezone'] 
        local_time = datetime.utcnow() + timedelta(seconds=timezone_offset)     # input city's current time

        print(f"City: {city}")
        print(f"Current Date and Time: {local_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Weather: {weather_desc.capitalize()}")
        print(f"Temperature: {main['temp']}°C")
        print(f"Temperature feels like: {main['feels_like']}°C")
        print(f"Humidity: {main['humidity']}%")
        print(f"Wind Speed: {wind['speed']} m/s")
    else:
        print(f"City {city} not found!")

# test with a city name from user
city_name = input("Enter city name: ")
get_weather(city_name)
