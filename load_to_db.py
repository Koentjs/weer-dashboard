from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()
DB_URL = os.getenv("DB_URL")
engine = create_engine(DB_URL)

def load_to_db(weather_data):
    with engine.connect() as conn:
        # Maak een tabel aan las die er nog niet is
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS weather_data (
            city TEXT,
            temperature NUMERIC,
            humidity INTEGER,
            wind_speed NUMERIC,
            timestamp TIMESTAMP
        )
        """))
        # Voeg data toe
        conn.execute(text("""
        INSERT INTO weather_data (city, temperature, humidity, wind_speed, timestamp)
        VALUES(:city, :temperature, :humidity, :wind_speed, :timestamp)
        """), weather_data)
        conn.commit()
    print("Data opgeslagen in database")

if __name__ == "__main__":
    # Voor Testdoeleinden
    test_data = {
        "city" : "Amsterdam",
        "temperature" : 20.5,
        "humidity" : 65,
        "wind_speed" : 3.5,
        "timestamp": "2025-08-06 15:00:00"
    }
    load_to_db(test_data)