
slownik = [
    {"imie": "Mateusz","wiek":6},
    {"imie": "Baltazar","wiek": 55},
    {"imie": "Pompeusz","wiek":35}
]
a = [x['imie'] for x in slownik]
print("imiona to: {} ".format(a))