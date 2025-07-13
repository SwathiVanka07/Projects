import requests

def get_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    # Parameters for API request
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # metric = Celsius
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raises HTTPError for 4xx and 5xx responses

        data = response.json()

        main = data['main']
        weather = data['weather'][0]

        temp = main['temp']
        humidity = main['humidity']
        description = weather['description']

        print(f"\nWeather in {city_name.title()}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {description.capitalize()}")

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print(f"\nCity '{city_name}' not found. Please check the spelling and try again.")
        elif response.status_code == 401:
            print("Invalid API key. Please check your key.")
        else:
            print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Network error occurred: {req_err}")
    except KeyError:
        print("Unexpected response format. Please try again later.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    
    api_key = "277353313a9d07cdb6a93d303dd8d52e"  # OpenWeatherMap API key is used
    get_weather(city, api_key)

