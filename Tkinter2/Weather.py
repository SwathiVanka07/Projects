import tkinter as tk
import requests
from tkinter import messagebox 

 
# OpenWeatherMap API key
API_KEY = "277353313a9d07cdb6a93d303dd8d52e"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name.")
        return
    
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        
        city_name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"].title()
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        result = (
            f"Weather in {city_name}, {country}:\n"
            f"Temperature: {temp}°C\n"
            f"Condition: {weather}\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind_speed} m/s"
        )

        result_label.config(text=result)

    except requests.exceptions.HTTPError:
        messagebox.showerror("Error", "City not found.")
    except requests.exceptions.RequestException:
        messagebox.showerror("Error", "Network error.")

# GUI setup
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")
root.resizable(False, False)

# Entry field
city_entry = tk.Entry(root, font=("Arial", 14))
city_entry.pack(pady=20)

# Button
search_btn = tk.Button(root, text="Get Weather", font=("Arial", 12), command=get_weather)
search_btn.pack()

# Result Label
result_label = tk.Label(root, font=("Arial", 12), justify="left", wraplength=350)
result_label.pack(pady=20)

root.mainloop()
