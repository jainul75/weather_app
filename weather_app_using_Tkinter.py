# libraries
import requests
import tkinter as tk
from tkinter import messagebox, ttk  # ttk for improved styling

API_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXX'  # replace with your OpenWeatherMap API key

# define function for getting weather data from API
def get_weather(city):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        wind = data['wind']
        weather_desc = data['weather'][0]['description']
        result = (
            f"City: {city}\n"
            f"Temperature: {main['temp']}°C\n"
            f"Temperature feels like: {main['feels_like']}°C\n"
            f"Humidity: {main['humidity']}%\n"
            f"Weather: {weather_desc.capitalize()}\n"
            f"Wind Speed: {wind['speed']} m/s\n"
        )
        return result
      
    elif response.status_code == 401:
      messagebox.showerror("Error", "Invalid API key! Please check your API key.")    # show error for API key issue or wrong API
    elif response.status_code == 404:
      messagebox.showerror("Error", f"City '{city}' not found!")      # show error in GUI, if user put wrong city name
    else:
      messagebox.showerror("Error", "An unexpected error occurred!")  # general error message
    return ""

# function for bring weather data according to user input city
def fetch_weather():
    cities = city_entry.get().split(',')
    results = []
    for city in cities:
        city = city.strip()
        weather_info = get_weather(city)
        results.append(weather_info)
    
    weather_text.config(state='normal')                 # allow editing to insert new content
    weather_text.delete('1.0', tk.END)                  # clear previous results
    weather_text.insert(tk.END, "\n\n".join(results))   # show results
    weather_text.config(state='disabled')               # disable editing again


# create GUI
app = tk.Tk()
app.title("Weather App")
app.geometry('500x500')  # set the window size

# define font styles
font_label = ("Poppins", 14)
font_entry = ("Poppins", 12)
font_button = ("Poppins", 16, "bold")

# city input label
input_frame = ttk.Frame(app, padding="10")
input_frame.pack(fill="x")

tk.Label(input_frame, text="Adan's Weather App", font=("Poppins", 17, "bold")).pack(pady=10)  # title

city_label = tk.Label(input_frame, text="Enter city names:\nTo get weather data for multiple cities, separate the names with commas.", 
                      font=font_label, justify="center")
city_label.pack(anchor="center", pady=5)

# city input field
city_entry = tk.Entry(input_frame, width=50, font=font_entry)
city_entry.pack(pady=10)

# fetch weather button
button_frame = ttk.Frame(app, padding="10")
button_frame.pack(fill="x")

fetch_button = tk.Button(button_frame, text="Get Weather", command=fetch_weather, bg="#4CAF50", fg="white", font=font_button)
fetch_button.pack(pady=10)

# weather output area with a scrollbar
output_frame = ttk.Frame(app, padding="10")
output_frame.pack(padx=20, pady=20)  

weather_text = tk.Text(output_frame, width=45, height=15, wrap="word", font=font_entry, state='disabled') 
scrollbar = tk.Scrollbar(output_frame, command=weather_text.yview)
weather_text.config(yscrollcommand=scrollbar.set)

weather_text.pack(side="left", fill="both", expand=True, padx=10, pady=10)  # padding around the text box
scrollbar.pack(side="right", fill="y")

# run the application
app.mainloop()
