import requests
from datetime import datetime

API_KEY = "b48c1dd53c205e418ef6134f3e34a80c"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def fetch_weather(city="Amsterdam"):
    print(f"Start fetching weather data for {city}...")
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    print(f"API response status code: {response.status_code}")

    if response.status_code != 200:
        print(f"Fout bij ophalen data: {response.text}")
        return None

    data = response.json()
    weather = {
        "city": city,
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "timestamp": datetime.utcnow()
    }
    print(f"Data opgehaald: {weather}")
    return weather

if __name__ == "__main__":
    result = fetch_weather()
    if result:
        print(result)
    else:
        print("Geen data opgehaald.")
