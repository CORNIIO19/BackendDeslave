import requests

def get_rain(lat, lon):

    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        f"&hourly=rain"
    )

    print("\n=== LLAMANDO OPEN METEO ===")
    print(url)

    r = requests.get(url, timeout=10)

    print("\n=== OPEN METEO RAW RESPONSE ===")
    print(r.text)
    print("=============================\n")

    data = r.json()

    try:
        rain_list = data["hourly"]["rain"]

        # acumulado próximas 24 horas
        total = sum(rain_list[:24])

        print("Rain next 24h:", total)

        return round(total, 2)

    except Exception as e:
        print("OpenMeteo error:", e)
        return 0