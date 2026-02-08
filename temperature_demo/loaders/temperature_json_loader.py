import json
from pathlib import Path

from temperature_demo.models.temperature_models import TemperatureDataset, TemperatureReading


def load_dataset(json_path: str | Path) -> TemperatureDataset:
    """Charge un dataset de température depuis un fichier JSON."""
    path = Path(json_path)
    raw = json.loads(path.read_text(encoding="utf-8"))
    return TemperatureDataset.model_validate(raw)


def load_readings_only(json_path: str | Path) -> list[TemperatureReading]:
    """Exemple 'découverte' : construire une liste d'objets depuis un sous-tableau JSON.

    Point clé :
        [Model.model_validate(item) for item in raw_list]
    """
    path = Path(json_path)
    raw = json.loads(path.read_text(encoding="utf-8"))

    # Ici on ne veut que la liste de mesures (readings)
    readings_payload = raw["readings"]

    # ✅ Syntaxe à retenir :
    return [TemperatureReading.model_validate(r) for r in readings_payload]
