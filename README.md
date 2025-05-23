# 🧾 Kalkulator PIT

**Graficzna aplikacja do obliczania podatku dochodowego (PIT) z wykresami i zapisem danych.**

---

## 📌 Opis programu

Aplikacja umożliwia:
- dodawanie nowych rozliczeń podatkowych,
- przegląd i porównywanie zapisanych danych,
- wizualizację wyników w formie wykresów (kołowy lub słupkowy),
- zapis i odczyt danych do/z pliku JSON,
- wygodny i przejrzysty interfejs dzięki użyciu biblioteki **CustomTkinter**.

Dane wejściowe:
- dochód brutto,
- składki ZUS,
- ulga internetowa.

---

## 👤 Autor

**Oliwia Laskowska**

---

## 🚀 Instrukcja uruchomienia

### ✅ 1. Pobranie i przejście do katalogu projektu

Jeśli korzystasz z VS Code, terminala PowerShell, CMD lub systemu Linux/macOS:

**W Windows (PowerShell, CMD, VS Code Terminal):**

```powershell
cd ŚCIEŻKA\DO\PROJEKTU
# Przykład:
cd C:\Users\TwojaNazwaUzytkownika\Desktop\Projekt_Aplikacja_Do_Obliczania_PIT
```

---

### ✅ 2. Utworzenie i aktywacja środowiska wirtualnego

#### 📍 Windows:

```powershell
python -m venv venv
.\venv\Scripts\activate
```

Jeśli pojawi się komunikat o ograniczeniach wykonywania skryptów:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# Następnie aktywuj ponownie środowisko:
.\venv\Scripts\activate
```

#### 🐧 Linux / 🍎 macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### ✅ 3. Instalacja wymaganych bibliotek

```bash
pip install -r requirements.txt
```

---

### ✅ 4. Uruchomienie programu

```bash
python main.py
```

---

### 📌 Wymagane biblioteki (lista z `requirements.txt`)

- customtkinter
- matplotlib
- numpy
- pillow
- i inne zależności wymagane do działania GUI i wykresów