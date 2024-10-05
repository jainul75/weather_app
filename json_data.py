# to check what JSON data is available from the OpenWeatherMap API for the current weather

import requests

# OpenWeatherMap API key
API_KEY = 'put_your_API_key'
city = 'Comilla'

base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
response = requests.get(base_url)

if response.status_code == 200:
    data = response.json()
    print(data)
