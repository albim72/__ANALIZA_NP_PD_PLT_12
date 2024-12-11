import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Wczytanie danych z pliku CSV
file_path = "wydatki_domowe.csv"
data = pd.read_csv(file_path, parse_dates=["data"])

# Dodanie kolumny "miesiac" do analizy miesięcznej
data["miesiac"] = data["data"].dt.to_period("M")

# Obliczenia:
# 1. Sumaryczne wydatki w roku
suma_wydatkow = data["kwota"].sum()

# 2. Kategoria z najwyższymi wydatkami
wydatki_kategorie = data.groupby("kategoria")["kwota"].sum()
kategoria_max_wydatki = wydatki_kategorie.idxmax()

# 3. Średnie miesięczne wydatki dla każdej kategorii
srednie_miesieczne_kategorie = data.groupby(["miesiac", "kategoria"])["kwota"].sum().unstack().mean()

# 4. Sumaryczne miesięczne wydatki
sumaryczne_miesieczne = data.groupby("miesiac")["kwota"].sum()

# Wizualizacja
plt.figure(figsize=(12, 6))

# Wykres liniowy - sumaryczne miesięczne wydatki
plt.subplot(1, 2, 1)
plt.plot(sumaryczne_miesieczne.index.astype(str), sumaryczne_miesieczne.values, marker="o", color="blue", label="Wydatki miesięczne")
plt.xlabel("Miesiąc")
plt.ylabel("Kwota (PLN)")
plt.title("Sumaryczne miesięczne wydatki")
plt.xticks(rotation=45)
plt.grid()
plt.legend()

# Wykres kołowy - udziały procentowe wydatków na kategorie
plt.subplot(1, 2, 2)
wydatki_kategorie.plot.pie(autopct="%1.1f%%", startangle=90, colors=plt.cm.tab10.colors)
plt.ylabel("")
plt.title("Udział wydatków na kategorie")

# Zapis wykresów jako plik PNG
plt.tight_layout()
plt.savefig("analiza_wydatkow_domowych.png")

# Wyświetlenie wyników w konsoli
print("Sumaryczne wydatki w roku: {:.2f} PLN".format(suma_wydatkow))
print("Kategoria z najwyższymi wydatkami: {}".format(kategoria_max_wydatki))
print("\nŚrednie miesięczne wydatki dla każdej kategorii:")
print(srednie_miesieczne_kategorie)
