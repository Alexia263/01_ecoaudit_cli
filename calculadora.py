"""Módulo de cálculo de impacto energético y huella de carbono."""


def estimar_consumo_wh(potencia_w: float, horas_uso: float, iteraciones: int = 1) -> float:
    """Calcula el consumo energético total en Wh."""
    return potencia_w * horas_uso * iteraciones


def calcular_huella_co2(consumo_wh: float, factor_emision: float = 0.23) -> float:
    """Calcula la huella de carbono estimada en gramos de CO2."""
    consumo_wh = consumo_wh / 1000.0
    huella = consumo_wh * factor_emision
    
    return huella