import requests  # for sending HTTP requests
from datetime import datetime, timedelta

# OpenWeatherMap API key 
API_KEY = 'XXXXXXXXXXXXXXXXXXXXXXX6XXX5'  # replace it with yours

# create a function to get the current weather
def get_weather(city):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(base_url)  # send request to the API
        response.raise_for_status()  # raise an error for bad responses (4xx or 5xx)

        data = response.json()  # convert response to JSON

        main = data['main']  # fetch temperature-related data
        wind = data['wind']
        weather_desc = data['weather'][0]['description']
        timezone_offset = data['timezone']
        local_time = datetime.utcnow() + timedelta(seconds=timezone_offset)  # city's current time

        # output
        weather_info = (
            f"City: {city}\n"
            f"Current Date and Time: {local_time.strftime('%A, %Y-%m-%d %H:%M:%S')}\n"
            f"Weather: {weather_desc.capitalize()}\n"
            f"Temperature: {main['temp']}°C\n"
            f"Temperature feels like: {main['feels_like']}°C\n"
            f"Humidity: {main['humidity']}%\n"
            f"Wind Speed: {wind['speed']} m/s\n"
        )
        return weather_info 

    except requests.exceptions.HTTPError as http_err:        # error handling 
        if response.status_code == 401:
            return "Error: Invalid API key! Please check your API key."
        elif response.status_code == 404:
            return f"Error: City '{city}' not found!"
        else:
            return f"HTTP error occurred: {http_err}"
    except Exception as err:
        return f"An error occurred: {err}"

# test with a city name input from the user
city_name = input("Enter city name: ")
weather_result = get_weather(city_name)

print(weather_result)
