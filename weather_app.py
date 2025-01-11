import requests # type: ignore

# Get your API key from OpenWeatherMap
API_KEY = '1ffc8abca64b6c0ab53f4d8d07ebcdf5'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        city = data['name']
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        
        print(f"\nWeather in {city}:")
        print(f"Description: {weather}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
    else:
        print("City not found or invalid API key.")

# Main Program
if __name__ == '__main__':
    while True:
        city = input("\nEnter city name (or type 'quit' to exit): ").strip()
        if city.lower() == 'quit':
            print("Goodbye!")
            break
        get_weather(city)
