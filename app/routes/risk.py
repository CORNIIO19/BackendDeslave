# from fastapi import APIRouter
# from app.services.weather import get_rain
# from app.services.nasa import get_nasa_rain
# from app.services.predictor import predict

# router = APIRouter()

# @router.get("/risk")
# def get_risk(lat: float, lon: float):
#     rain = get_rain(lat, lon)
#     nasa = get_nasa_rain(lat, lon)

#     result = predict(rain, nasa)

#     return {
#         "rain": rain,
#         "nasa": nasa,
#         "risk": result
#     }

# app/routes/risk.py

from fastapi import APIRouter
from app.services.weather import get_rain
from app.services.nasa import get_nasa_rain
from app.services.predictor import combine, predict
from app.services.cache import get, set
import asyncio

router = APIRouter()

# Funciones de seguridad para que el MVP no falle si la API externa falla
async def safe_get_rain(lat: float, lon: float) -> float:
    try:
        return await get_rain(lat, lon)
    except Exception as e:
        print("ERROR Open-Meteo:", e)
        return 0.0

async def safe_get_nasa(lat: float, lon: float) -> float:
    try:
        return await get_nasa_rain(lat, lon)
    except Exception as e:
        print("ERROR NASA POWER:", e)
        return 0.0

@router.get("/risk")
async def risk(lat: float, lon: float):
    key = f"{lat}:{lon}"

    # 1️⃣ Revisar cache primero
    cached = get(key)
    if cached:
        return cached

    # 2️⃣ Llamar a las APIs en paralelo con fallback
    rain, nasa = await asyncio.gather(
        safe_get_rain(lat, lon),
        safe_get_nasa(lat, lon)
    )

    # 3️⃣ Ponderación y predicción
    combined = combine(rain, nasa)
    risk_level = predict(combined)

    # 4️⃣ Construir resultado
    result = {
        "rain": rain,
        "nasa": nasa,
        "combined": combined,
        "risk": risk_level
    }

    # 5️⃣ Guardar en cache
    set(key, result)

    return result

