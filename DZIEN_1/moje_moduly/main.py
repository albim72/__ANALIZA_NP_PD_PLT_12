# import dane
# import dane as dn
from dane import nr_filii as nf
from dane import book as bk
from funkcje.mojefunkcje import czytaj_liste,czytaj_slownik

#CTRL + D -> duplikacja liniibloku tekstu
#CTRL + / -> szybkie komentowane linii/bloku
print("___________________ DANE ___________________")
print(nf)
print(bk)

print("___________________ FUNKCJE ___________________")
czytaj_liste(nf)
czytaj_slownik(bk)
