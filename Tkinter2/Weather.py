from flask import Flask, render_template, request
import requests

# Create the Flask application
app = Flask(__name__)

API_KEY = "277353313a9d07cdb6a93d303dd8d52e"  # OpenWeatherMap API key

# Function to get weather data from OpenWeatherMap
def get_weather(city_name):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,      # City name entered by the user
        "appid": API_KEY,      # API key to authenticate
        "units": "metric"        # Use Celsius for temperature
    }
    try:
        response = requests.get(base_url, params=params)   # Make a GET request to the weather API
        response.raise_for_status()    # Raise exception for bad responses (4xx or 5xx)
        data = response.json()

        main = data['main']      # Extract main weather data
        weather = data['weather'][0]

        return {
            "city": city_name.title(),        # city name
            "temperature": main['temp'],       # Current temperature

            "humidity": main['humidity'],         # Humidity level
            "description": weather['description'].capitalize()
        }
         
          # Handle specific HTTP errors
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            return {"error": f"City '{city_name}' not found. Please check the spelling and try again."}
        elif response.status_code == 401:
            return {"error": "Invalid API key. Please check your key."}
        else:
            return {"error": f"HTTP error occurred: {http_err}"}
      
      # Handle other request errors (like no internet)
    except requests.exceptions.RequestException as req_err:
        return {"error": f"Network error occurred: {req_err}"}
    
    except KeyError:
        return {"error": "Unexpected response format. Please try again later."}  # Handle unexpected data 

@app.route('/', methods=['GET', 'POST'])  # Main route to handle both GET (page load) and POST (form submit)
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            weather_data = get_weather(city)    # get weather for the entered city
    return render_template('index.html', weather=weather_data)

if __name__ == '__main__':
    app.run(debug=True)     # Run the app

