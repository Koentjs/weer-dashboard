from fetch_weather import fetch_weather
from load_to_db import load_to_db

def main():
    weather = fetch_weather()
    load_to_db(weather)

if __name__ == "__main__":
    main()