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



bk = Book(26,"Moje Góry","Jan Byrcyn",45)
print(bk)
bk("promocja przesunięta na dzień 15.01.2025!")

