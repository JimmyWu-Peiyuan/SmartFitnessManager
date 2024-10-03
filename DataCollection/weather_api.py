import requests

# API key directly in the script (Not recommended for security reasons)
WEATHERAPI_KEY = '833822cc41704d9cb4d174049241709'

def get_weather(location):
    # Construct the API URL
    base_url = "http://api.weatherapi.com/v1/current.json"
    params = {
        'key': WEATHERAPI_KEY,
        'q': location
    }

    try:
        # Make the API request
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Parse the JSON response
        weather_data = response.json()
        
        return weather_data
    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
        return None

def display_weather(weather_data):
    if weather_data:
        location = weather_data['location']
        current = weather_data['current']
        
        print(f"\nWeather in {location['name']}, {location['country']}:")
        print(f"Temperature: {current['temp_c']}°C ({current['temp_f']}°F)")
        print(f"Condition: {current['condition']['text']}")
        print(f"Humidity: {current['humidity']}%")
        print(f"Wind: {current['wind_kph']} km/h, {current['wind_dir']}")
    else:
        print("Unable to retrieve weather data.")

def main():
    while True:
        location = input("\nEnter a city name (or 'quit' to exit): ")
        
        if location.lower() == 'quit':
            print("Goodbye!")
            break
        
        weather_data = get_weather(location)
        display_weather(weather_data)

if __name__ == "__main__":
    main()