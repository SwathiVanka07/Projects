from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "277353313a9d07cdb6a93d303dd8d52e"  # Your OpenWeatherMap API key

def get_weather(city_name):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        main = data['main']
        weather = data['weather'][0]

        return {
            "city": city_name.title(),
            "temperature": main['temp'],
            "humidity": main['humidity'],
            "description": weather['description'].capitalize()
        }

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            return {"error": f"City '{city_name}' not found. Please check the spelling and try again."}
        elif response.status_code == 401:
            return {"error": "Invalid API key. Please check your key."}
        else:
            return {"error": f"HTTP error occurred: {http_err}"}
    except requests.exceptions.RequestException as req_err:
        return {"error": f"Network error occurred: {req_err}"}
    except KeyError:
        return {"error": "Unexpected response format. Please try again later."}

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            weather_data = get_weather(city)
    return render_template('index.html', weather=weather_data)

if __name__ == '__main__':
    app.run(debug=True)

