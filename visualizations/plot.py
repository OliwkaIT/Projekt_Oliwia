import matplotlib.pyplot as plt
import numpy as np
from functions.tax_calc import oblicz_podatek

# Tworzy wykres na podstawie wyniku — kołowy lub słupkowy
def rysuj_wykres(wynik, typ="kołowy"):
    labels = ['Podatek', 'ZUS', 'Netto']
    values = [wynik['podatek'], wynik['zus'], wynik['netto']]

    fig, ax = plt.subplots()

    # Styl ciemnego tła — pasuje do GUI
    fig.patch.set_facecolor('#1e1e1e')
    ax.set_facecolor('#1e1e1e')
    ax.tick_params(colors='white')
    for spine in ax.spines.values():
        spine.set_color('white')

    if typ == "kołowy":
        ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, textprops={'color':"white"})
        ax.axis('equal')  # Koło zamiast elipsy
    elif typ == "słupkowy":
        ax.bar(labels, values, color=['red', 'blue', 'green'])
        ax.set_ylabel("Kwota (zł)")
        ax.set_title("Rozkład kosztów", color="white")
    else:
        ax.text(0.5, 0.5, "Nieznany typ wykresu", ha='center', color='white')

    return fig

# Przykładowy wykres liniowy pokazujący wzrost podatku
def rysuj_przyklad_liniowy():
    dochody = np.arange(0, 2_000_001, 10_000)
    podatki = []

    for dochod in dochody:
        wynik = oblicz_podatek(dochod, 0, 0)
        podatki.append(wynik['podatek'])

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(dochody, podatki, label="Podatek", color="cyan")
    ax.set_title("Wzrost podatku wraz z dochodem", color="white")
    ax.set_xlabel("Dochód brutto [zł]", color="white")
    ax.set_ylabel("Podatek [zł]", color="white")
    ax.grid(True, linestyle='--', alpha=0.5)

    fig.patch.set_facecolor('#1e1e1e')
    ax.set_facecolor('#1e1e1e')
    ax.tick_params(colors='white')
    for spine in ax.spines.values():
        spine.set_color('white')

    ax.legend(facecolor="#1e1e1e", edgecolor="white", labelcolor="white")

    return fig
