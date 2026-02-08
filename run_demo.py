from temperature_demo.loaders.temperature_json_loader import load_dataset, load_readings_only


def main() -> None:
    dataset = load_dataset("data/temperature.json")
    print("Dataset chargé (objet complet) :")
    print(f"  city={dataset.city} unit={dataset.unit} nb_readings={len(dataset.readings)}")
    print(f"  première mesure: {dataset.readings[0].timestamp} -> {dataset.readings[0].value}")

    readings = load_readings_only("data/temperature.json")
    print("\nListe de mesures chargée (list comprehension + model_validate) :")
    for r in readings:
        print(f"  {r.timestamp} -> {r.value}")


if __name__ == "__main__":
    main()
