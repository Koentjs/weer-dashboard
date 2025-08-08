# scheduler.py
from fetch_weather import fetch_weather
from load_to_db import load_to_db

def main():
    print("Job gestart...")
    weather_data = fetch_weather()
    load_to_db(weather_data)
    print("Weerdata opgehaald en opgeslagen")

if __name__ == "__main__":
    main()
