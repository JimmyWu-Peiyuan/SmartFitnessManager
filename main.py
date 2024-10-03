from DataCollection.weather_api import *
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