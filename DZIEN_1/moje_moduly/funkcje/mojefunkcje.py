def czytaj_liste(lista):
    for i,j in enumerate(lista):
        print(f"Element listy {i} o wartości: {j}")
        
def czytaj_slownik(slownik):
    for x,y in slownik.items():
        print(f"klucz: {x} -> wartość: {y}")
