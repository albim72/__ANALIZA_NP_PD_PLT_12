import re

#szukanie fraz

#metoda 1
text = "Witaj w świecie Python! Python to piękny język. Kierunek - Python."
phrase = "Python"

if phrase in text:
    print(f'fraza {phrase} została znaleziona')
else:
    print(f'fraza {phrase} nie znaleziona')

#metoda 2
index = text.find(phrase)

if index != -1:
    print(f"fraza {phrase} znaleziona na indeksie {index}")
else:
    print(f'fraza {phrase} nie znaleziona')

#metoda 3
match = re.search(phrase, text, re.IGNORECASE)
if match:
    print(f"fraza {match.group()} znaleziona na indeksie {match.start()}")
else:
    print(f'fraza {phrase} nie znaleziona')

#wypisz każde z wystąpień
matches = re.finditer(phrase, text, re.IGNORECASE)
print("Wystąpienia frazy:")
for match in matches:
    print(f"\tFraza {match.group()} na indeksie {match.start()} - {match.end()}")

#szukanie adresów e-mail w tekście
emailtext = """
Skontaktuj się z nami pod adresem support@example.pl lub admin@domain.org.
Możesz także napisać na adres: kontakt@firma.pl lub ad+@p.pl, info@oper.com.pl, takie@abc.com.
"""

#wzorzec
e_mail_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-.]+[a-zA-Z0-9-]+'

#wyszukiwanie maili
emails = re.findall(e_mail_pattern, emailtext)
print("znalezione adresy email: ")
for email in emails:
    print(f"\t{email}")
