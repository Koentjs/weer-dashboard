from fetch_weather import fetch_weather
from load_to_db import load_to_db

def main():
    print("Start pipeline...")
    weather = fetch_weather()
    if weather is None:
        print("Geen weerdata opgehaald, stop pipeline.")
        return
    load_to_db(weather)
    print("Pipeline afgerond.")

if __name__ == "__main__":
    main()
