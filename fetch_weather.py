import requests
from datetime import datetime

API_KEY = "b48c1dd53c205e418ef6134f3e34a80c"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def fetch_weather(city="Amsterdam"):
    params = {
        "q" : city,
        "appid" : API_KEY,
        "units" : "metric"
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    weather = {
        "city" : city,
        "temperature": data["main"] ["temp"],
        "humidity": data["main"] ["humidity"],
        "wind_speed": data["wind"] ["speed"],
        "timestamp": datetime.utcnow()
    }
    return weather

if __name__ == "__main__":
    print(fetch_weather())