# app/services/cache.py

import time

# Diccionario interno para almacenar los datos en memoria
_cache = {}

def get(key: str):
    """
    Obtiene el valor del cache por su clave.
    Devuelve None si la clave no existe o ya expiró.
    """
    item = _cache.get(key)
    if not item:
        return None

    value, expires = item

    # Verifica si el valor expiró
    if time.time() > expires:
        del _cache[key]
        return None

    return value


def set(key: str, value, ttl: int = 300):
    """
    Guarda un valor en el cache.
    ttl: tiempo de vida en segundos (por defecto 5 minutos)
    """
    _cache[key] = (value, time.time() + ttl)
