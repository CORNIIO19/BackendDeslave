import requests
from datetime import datetime, timedelta

NASA_URL = "https://power.larc.nasa.gov/api/temporal/daily/point"

def get_nasa_rain(lat, lon):
    today = datetime.now()
    start = (today - timedelta(days=5)).strftime("%Y%m%d")
    end = (today - timedelta(days=1)).strftime("%Y%m%d")

    params = {
        "parameters": "PRECTOTCORR",
        "community": "RE",
        "longitude": lon,
        "latitude": lat,
        "start": start,
        "end": end,
        "format": "JSON"
    }

    r = requests.get(NASA_URL, params=params, timeout=10)
    data = r.json()

    try:
        values = data["properties"]["parameter"]["PRECTOTCORR"]

        # recorrer del más reciente al más viejo
        for v in reversed(list(values.values())):
            if v != -999:
                return v

        return 0

    except Exception as e:
        print("NASA error:", e)
        return 0
