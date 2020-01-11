x = 'Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak A' \
    'ldus PageMaker'
	
imie='Karol'
nazwisko='Wawrzyszczak'
litera_1=imie[2]
litera_2=nazwisko[3]

licznik1=x.count(litera_1) 

licznik2=x.count(litera_2)

odp='w tekscie jest {} liter {} oraz {} liter {} '.format(licznik1,litera_1,licznik2,litera_2)
print(odp)

