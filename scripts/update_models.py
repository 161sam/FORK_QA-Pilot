import requests
import configparser

# Basis-URL der LM Studio API
BASE_URL = "http://192.168.0.221:1234/v1/models"

# Funktion zum Abrufen der Modelle
def get_models():
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
        models = response.json()  # Annahme: Die API gibt JSON zurück
        return models.get("models", [])  # Annahme: Modelle sind unter "models" gelistet
    except Exception as e:
        print(f"Fehler beim Abrufen der Modelle: {e}")
        return []

# Funktion zum Aktualisieren der config.ini
def update_config(models):
    config = configparser.ConfigParser()
    config.read("config/config.ini")

    # Aktualisieren des model_list und selected_model
    config["lm-studio_llm_models"]["model_list"] = ", ".join(models)
    if models:
        config["lm-studio_llm_models"]["selected_model"] = models[0]  # Erstes Modell auswählen

    # Änderungen speichern
    with open("config/config.ini", "w") as configfile:
        config.write(configfile)
    print("config.ini wurde aktualisiert.")

# Hauptlogik
if __name__ == "__main__":
    models = get_models()
    if models:
        print(f"Gefundene Modelle: {models}")
        update_config(models)
    else:
        print("Keine Modelle gefunden.")
