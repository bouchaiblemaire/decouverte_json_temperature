from __future__ import annotations

from typing import List
from pydantic import BaseModel, Field


class TemperatureReading(BaseModel):
    """Une mesure de température à un instant donné."""

    timestamp: str = Field(..., description="Horodatage ISO-8601 (string pour simplifier la démo).")
    value: float = Field(..., description="Valeur numérique de la température.")


class TemperatureDataset(BaseModel):
    """Dataset complet : ville, unité et liste de mesures."""

    city: str = Field(..., min_length=1)
    unit: str = Field(..., min_length=1, description="Ex: C, F")
    readings: List[TemperatureReading] = Field(..., min_length=1)
