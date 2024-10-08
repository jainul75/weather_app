import requests
from datetime import datetime, timedelta
from flask import Flask, render_template, request

app = Flask(__name__)

# OpenWeatherMap API key, replace it with yours
API_KEY = 'XXXXXXAAAAAAAAAAAAXXXXXXXXXX'  

# function to get current weather
def get_weather(city):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(base_url)       # send request to the API
        response.raise_for_status()
        data = response.json()                  # convert response to JSON

        main = data['main']                     # fetching weather data
        wind = data['wind']
        weather_desc = data['weather'][0]['description']
        timezone_offset = data['timezone']
        local_time = datetime.utcnow() + timedelta(seconds=timezone_offset)     # city's current time
        t_date = local_time.strftime('%Y-%m-%d')  # extract the date

        weather_info = {
            "city": city,
            'date': t_date,
            "date_time": local_time.strftime('%A, %H:%M:%S'),
            "description": weather_desc.capitalize(),
            "temp": main['temp'],
            "feels_like": main['feels_like'],
            "humidity": main['humidity'],
            "wind_speed": wind['speed'],
        }
        return weather_info 

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 401:
            return {"error": "Invalid API key! Please check your API key."}
        elif response.status_code == 404:
            return {"error": f"City '{city}' not found!"}
        else:
            return {"error": f"HTTP error occurred: {http_err}"}
    except Exception as err:
        return {"error": f"An error occurred: {err}"}

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city_name = request.form.get('city_name')
        weather_data = get_weather(city_name)
    return render_template('index.html', weather=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
