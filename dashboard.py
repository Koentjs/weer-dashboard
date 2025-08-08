import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

#laat environment variables uit .env
load_dotenv()
DB_URL = os.getenv("DB_URL")

# Controleer of de URL werd opgehaald
if not DB_URL:
    raise ValueError("DB_URL is niet ingesteld in secrets!")

#maak database connectie
engine = create_engine(DB_URL)

@st.cache_data
def load_data():
    query = "SELECT * FROM weather_data ORDER BY timestamp DESC LIMIT 1000;"
    df = pd.read_sql(query, engine)
    return df

st.title("Weerdata Dashboard")

data = load_data()

st.write("Laatste weermetingen:")
st.dataframe(data)

if not data.empty:
    st.subheader("Temperatuur over tijd")
    st.line_chart(data.sort_values("timestamp")[["timestamp", "temperature"]].set_index("timestamp"))

    st.subheader("Luchtvochtigheid over tijd")
    st.line_chart(data.sort_values("timestamp")[["timestamp", "humidity"]].set_index("timestamp"))
else:
    st.warning("Geen data gevonden in de database")