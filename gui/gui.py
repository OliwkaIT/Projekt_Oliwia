import customtkinter as ctk
import tkinter.messagebox
from functions.tax_calc import oblicz_podatek
from visualizations.plot import rysuj_wykres, rysuj_przyklad_liniowy
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from saves.save import zapisz_rozliczenia, wczytaj_rozliczenia
import matplotlib.pyplot as plt

# Wczytujemy wcześniej zapisane rozliczenia (jeśli są)
rozliczenia = wczytaj_rozliczenia()

def start_gui():
    global rozliczenia
    rozliczenia = wczytaj_rozliczenia()

    # Ustawiamy wygląd aplikacji
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    # Wrzuca wykres do wskazanego frame'a i czyści poprzedni
    def rysuj_do_frame(fig, frame):
        for widget in frame.winfo_children():
            widget.destroy()
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

    # Dodaje nowe rozliczenie na podstawie danych z lewej strony
    def dodaj_rozliczenie():
        try:
            nazwa = entry_nazwa.get()
            dochod = float(entry_dochod.get())
            zus = float(entry_zus.get())
            ulga = float(entry_ulga.get())
            typ = wykres_var_lewy.get()

            # Sprawdzenie czy podano nazwę
            if not nazwa:
                tkinter.messagebox.showwarning("Brak nazwy", "Wprowadź nazwę rozliczenia.")
                return

            # Nie pozwalamy na duplikaty
            if nazwa in rozliczenia:
                tkinter.messagebox.showwarning("Istnieje", "Rozliczenie o takiej nazwie już istnieje.")
                return

            # Zapisujemy dane
            rozliczenia[nazwa] = {"dochod": dochod, "zus": zus, "ulga": ulga}
            zapisz_rozliczenia(rozliczenia)

            # Aktualizacja listy wyboru
            lista_rozliczen.configure(values=list(rozliczenia.keys()))
            lista_rozliczen.set("")

            # Obliczenie podatku i pokazanie wyniku
            wynik = oblicz_podatek(dochod, zus, ulga)
            label_wynik_lewy.configure(text=f"Podatek: {wynik['podatek']} zł | Netto: {wynik['netto']} zł")

            # Generowanie wykresu
            fig = rysuj_wykres(wynik, typ)
            rysuj_do_frame(fig, frame_wykres_lewy)

        except ValueError:
            tkinter.messagebox.showerror("Błąd", "Wprowadź poprawne liczby.")

    # Pokazuje dane istniejącego rozliczenia (prawa strona)
    def wybierz_rozliczenie():
        nazwa = lista_rozliczen.get()
        typ = wykres_var_prawy.get()

        if nazwa in rozliczenia:
            dane = rozliczenia[nazwa]
            wynik = oblicz_podatek(dane["dochod"], dane["zus"], dane["ulga"])

            label_wynik_prawy.configure(
                text=f"Dochód: {dane['dochod']} zł | ZUS: {dane['zus']} zł | Ulga: {dane['ulga']} zł\n"
                     f"Podatek: {wynik['podatek']} zł | Netto: {wynik['netto']} zł"
            )

            fig = rysuj_wykres(wynik, typ)
            rysuj_do_frame(fig, frame_wykres_prawy)

    # Usuwa wybrane rozliczenie
    def usun_rozliczenie():
        nazwa = lista_rozliczen.get()
        if nazwa in rozliczenia:
            del rozliczenia[nazwa]
            zapisz_rozliczenia(rozliczenia)
            lista_rozliczen.configure(values=list(rozliczenia.keys()))
            lista_rozliczen.set("")
            label_wynik_prawy.configure(text="")
            for widget in frame_wykres_prawy.winfo_children():
                widget.destroy()
            tkinter.messagebox.showinfo("Usunięto", f"Usunięto {nazwa}")
        else:
            tkinter.messagebox.showerror("Błąd", "Nie wybrano rozliczenia do usunięcia.")

    # Tworzenie głównego okna
    root = ctk.CTk()
    root.title("Kalkulator PIT")

    def on_closing():
        plt.close('all') # zamyka wykresy
        root.quit()   
        root.destroy()  # usuwa okno

    root.protocol("WM_DELETE_WINDOW", on_closing)

    # Lewy panel — dodawanie nowego rozliczenia
    left_frame = ctk.CTkFrame(master=root, corner_radius=10)
    left_frame.pack(side="left", padx=20, pady=20, fill="both", expand=True)

    # Prawy panel — przegląd i analiza istniejących
    right_frame = ctk.CTkFrame(master=root, corner_radius=10)
    right_frame.pack(side="right", padx=20, pady=20, fill="both", expand=True)

    # Pola wejściowe — lewa strona
    entry_nazwa = ctk.CTkEntry(left_frame, placeholder_text="Nazwa rozliczenia")
    entry_nazwa.pack(pady=5)

    entry_dochod = ctk.CTkEntry(left_frame, placeholder_text="Dochód brutto")
    entry_dochod.pack(pady=5)

    entry_zus = ctk.CTkEntry(left_frame, placeholder_text="Składki ZUS")
    entry_zus.pack(pady=5)

    entry_ulga = ctk.CTkEntry(left_frame, placeholder_text="Ulga internetowa")
    entry_ulga.pack(pady=5)

    wykres_var_lewy = ctk.StringVar(value="kołowy")
    combobox_lewy = ctk.CTkOptionMenu(left_frame, variable=wykres_var_lewy, values=["kołowy", "słupkowy"])
    combobox_lewy.pack(pady=5)

    ctk.CTkButton(left_frame, text="Dodaj rozliczenie", command=dodaj_rozliczenie).pack(pady=10)

    label_wynik_lewy = ctk.CTkLabel(left_frame, text="", font=("Arial", 12))
    label_wynik_lewy.pack(pady=5)

    frame_wykres_lewy = ctk.CTkFrame(left_frame)
    frame_wykres_lewy.pack(fill="both", expand=True, padx=10, pady=10)

    # Prawa strona — wybór istniejących rozliczeń i analiza
    lista_rozliczen = ctk.CTkComboBox(right_frame, values=[], state="readonly")
    lista_rozliczen.pack(pady=5)
    lista_rozliczen.configure(values=list(rozliczenia.keys()))  # Ładujemy zapisane nazwy

    wykres_var_prawy = ctk.StringVar(value="kołowy")
    combobox_prawy = ctk.CTkOptionMenu(right_frame, variable=wykres_var_prawy, values=["kołowy", "słupkowy"])
    combobox_prawy.pack(pady=5)

    ctk.CTkButton(right_frame, text="Pokaż wykres", command=wybierz_rozliczenie).pack(pady=5)
    ctk.CTkButton(right_frame, text="Usuń rozliczenie", command=usun_rozliczenie).pack(pady=5)

    label_wynik_prawy = ctk.CTkLabel(right_frame, text="", font=("Arial", 12))
    label_wynik_prawy.pack(pady=5)

    frame_wykres_prawy = ctk.CTkFrame(right_frame)
    frame_wykres_prawy.pack(fill="both", expand=True, padx=10, pady=10)

    # Wstępny wykres poglądowy (jak rośnie podatek)
    fig_przyklad = rysuj_przyklad_liniowy()
    rysuj_do_frame(fig_przyklad, frame_wykres_prawy)
    label_wynik_prawy.configure(text="Przykład: jak rośnie podatek od 0 do 2 mln zł")

     

    root.mainloop()
    
