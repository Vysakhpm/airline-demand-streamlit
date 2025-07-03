# opensky_api.py
import requests
import pandas as pd

def fetch_flight_data():
    url = "https://opensky-network.org/api/states/all"
    try:
        res = requests.get(url, timeout=10)
        data = res.json()

        flights = data.get("states", [])[:100]  # limit for speed
        df = pd.DataFrame(flights, columns=[
            "icao24", "callsign", "origin_country", "time_position",
            "last_contact", "longitude", "latitude", "baro_altitude",
            "on_ground", "velocity", "heading", "vertical_rate",
            "sensors", "geo_altitude", "squawk", "spi", "position_source"
        ])
        return df
    except Exception as e:
        print("Error fetching data:", e)
        return pd.DataFrame()
