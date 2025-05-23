# Prosta funkcja do obliczania podatku PIT według polskich progów
def oblicz_podatek(dochod_brutto, zus=0.0, ulga=0.0):
    kwota_wolna = 30000
    kwota_zmniejszajaca_podatek = 3600
    podstawa_opodatkowania = max(dochod_brutto - kwota_wolna - zus - ulga, 0)

    if podstawa_opodatkowania <= 120000:
        podatek = 0.12 * podstawa_opodatkowania - kwota_zmniejszajaca_podatek
    else:
        podatek = 0.12 * 120000 - kwota_zmniejszajaca_podatek + 0.32 * (podstawa_opodatkowania - 120000)

    podatek = max(podatek, 0)  # Nie pozwalamy na ujemny podatek
    dochod_netto = dochod_brutto - podatek - zus

    return {
        'dochod': dochod_brutto,
        'podatek': round(podatek, 2),
        'netto': round(dochod_netto, 2),
        'zus': round(zus, 2),
        'ulga': round(ulga, 2)
    }
