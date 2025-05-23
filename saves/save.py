import os
import json

# Ścieżka zapisu danych użytkownika
FOLDER_SAVES = "saves"
PLIK_ROZLICZEN = os.path.join(FOLDER_SAVES, "rozliczenia.json")

# Tworzymy folder, jeśli go nie ma
os.makedirs(FOLDER_SAVES, exist_ok=True)

# Zapisuje dane do pliku JSON
def zapisz_rozliczenia(rozliczenia):
    with open(PLIK_ROZLICZEN, "w", encoding="utf-8") as f:
        json.dump(rozliczenia, f, ensure_ascii=False, indent=4)

# Odczytuje dane z pliku JSON
def wczytaj_rozliczenia():
    if os.path.exists(PLIK_ROZLICZEN):
        with open(PLIK_ROZLICZEN, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}
