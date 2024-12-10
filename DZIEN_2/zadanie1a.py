from datetime import datetime

class Samochod:
    def __init__(self, marka: str, model: str, rocznik: int):
        self.marka = marka
        self.model = model
        self.rocznik = rocznik

    def __repr__(self):
        return f"Samochod(marka='{self.marka}', model='{self.model}', rocznik={self.rocznik})"

    def wiek_samochodu(self):
        aktualny_rok = datetime.now().year
        return aktualny_rok - self.rocznik

    def opis_samochodu(self):
        return f"{self.marka} {self.model}, rocznik {self.rocznik}"

# Przykład użycia:
samochod = Samochod("Toyota", "Corolla", 2015)
print(samochod)  # Wyświetli: Samochod(marka='Toyota', model='Corolla', rocznik=2015)
print(f"Wiek samochodu: {samochod.wiek_samochodu()} lat")  # Wyświetli wiek samochodu
print(samochod.opis_samochodu())  # Wyświetli: Toyota Corolla, rocznik 2015
