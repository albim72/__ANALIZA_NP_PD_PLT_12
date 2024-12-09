print("Język Python 3.X")

a:int = 700
print(a)
print(a.bit_length())
print(type(a))

a = "jedynka"
print(a)
print(type(a))
print(a.upper())

#kolekcje w pythonie -> lista,krotka,zbiór,słownik
"""
komantarz wieloliniowy
dokumentacyjny
"""

opis = """
to jest długi string
kilka linii
trzecia linia: 43765859375493
"""

print(opis)

#lista i krotka
cyfry = [5,2,6,2,89,4,2,4,-3,5]
imiona = ("Jan","Anna","Anna","Jacek")

print(cyfry)
print(type(cyfry))

print(imiona)
print(type(imiona))

mix = [5,True,"One",99.4,12,"Kraków"]
print(mix)
print(mix[0])
print(mix[3])
print(mix[2:5])
print(mix[-1])

print(imiona[3])

mix.append(False)
# imiona.append("Jan")
print(mix)

mix.remove(True)
print(mix)

cyfry.sort()
print(cyfry)

# mix.sort()  nie możemy sortować list mieszanych!

nlista = [[23,52],[[54,34,32,78],3],5,8,5,32]
# nlista.sort()
print(nlista)
print(nlista[1])
print(nlista[1][0])
print(nlista[1][0][2])
