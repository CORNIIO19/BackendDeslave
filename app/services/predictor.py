# from app.services.weather import get_rain

#     # app/services/predictor.py

# def combine(rain: float, nasa: float) -> float:
#     """
#     Combina la lluvia de Open-Meteo y NASA con ponderación simple.
#     Ajusta los pesos según sea necesario.
#     """
#     weight_rain = 0.7
#     weight_nasa = 0.3

#     return rain * weight_rain + nasa * weight_nasa


# def predict(value: float) -> str:
#     """
#     Determina riesgo según valor combinado de lluvia.
#     Ajusta umbrales según datos históricos o necesidades.
#     """
#     if value < 5:
#         return "bajo"
#     elif value < 20:
#         return "medio"
#     else:
#         return "alto"


# app/services/predictor.py

def combine(rain: float, nasa: float) -> float:
    """
    Combina la lluvia de Open-Meteo y NASA con ponderación simple.
    Ajusta los pesos según sea necesario.
    """
    weight_rain = 0.7
    weight_nasa = 0.3

    return rain * weight_rain + nasa * weight_nasa


def predict(value: float) -> str:
    """
    Determina riesgo según valor combinado de lluvia.
    Ajusta umbrales según datos históricos o necesidades.
    """
    if value < 5:
        return "bajo"
    elif value < 20:
        return "medio"
    else:
        return "alto"