class Book:
    #definicja stanu  - konstruktor klasy

    # def __new__(cls, *args, **kwargs):
    #     return object.__new__(Book)

    def __init__(self,id,tytul,autor,cena=30):
        self.idbook = id
        self.tytul = tytul
        self.autor = autor
        self.cena = cena
        self.oprawa = "miękka"
        self.create_book()

    def __repr__(self):
        return (f"Książka -> {self.tytul}, autor: {self.autor}, cena: {self.cena} zł, "
                f"okładka: {self.oprawa}")

    def __call__(self,messsage):
        print(f"Ważna wiadmość: {messsage} -> dotyczy ksiązki: {self.idbook} {self.tytul}")

    def create_book(self):
        print("Utworzono obiekt klasy Book!(nową książkę)")

    def get_cena(self):
        return self.cena

    def set_cena(self,nowacena):
        self.cena = nowacena

    @property
    def oprawa(self):
        return self._oprawa

    @oprawa.setter
    def oprawa(self,nowaoprawa):
        self._oprawa = nowaoprawa


bk = Book(26,"Moje Góry","Jan Byrcyn",45)
print(bk)
bk("promocja przesunięta na dzień 15.01.2025!")
# bk.cena = 48
# print(f"cena po zmianie: {bk.cena}")

bk.set_cena(48)
print(f"cena po zmianie: {bk.get_cena()}")
print(f"oprawa przed zmianą: {bk.oprawa}")
bk.oprawa = "twarda"
print(f"oprawa po zmianie: {bk.oprawa}")





