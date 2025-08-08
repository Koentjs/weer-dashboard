from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()
DB_URL = os.getenv("DB_URL")
print(f"DB_URL geladen: {DB_URL[:20]}...")  # Deel van URL tonen ivm veiligheid
engine = create_engine(DB_URL)

def load_to_db(weather_data):
    print("Start connectie met database...")
    with engine.connect() as conn:
        print("Connectie succesvol, maak tabel aan als nodig...")
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS weather_data (
            city TEXT,
            temperature NUMERIC,
            humidity INTEGER,
            wind_speed NUMERIC,
            timestamp TIMESTAMP
        )
        """))
        print("Tabel gecontroleerd, voeg data toe...")
        conn.execute(text("""
        INSERT INTO weather_data (city, temperature, humidity, wind_speed, timestamp)
        VALUES(:city, :temperature, :humidity, :wind_speed, :timestamp)
        """), weather_data)
        conn.commit()
        print("Data succesvol toegevoegd en commit uitgevoerd.")
    print("Connectie gesloten, data opgeslagen in database")

if __name__ == "__main__":
    # Voor testdoeleinden
    test_data = {
        "city" : "Amsterdam",
        "temperature" : 20.5,
        "humidity" : 65,
        "wind_speed" : 3.5,
        "timestamp": "2025-08-06 15:00:00"
    }
    print("Start test data laden...")
    load_to_db(test_data)
    print("Test data laden voltooid.")
