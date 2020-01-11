a=((123,'Karol Wawrzyszczak'),(312,'Michał Kowalski'),(456,'Tomek parobek')) 

slownik = dict((x,y) for x,y in a )   
slownik2 = {'Ostroleka':664674004}
slownik.update(slownik2)
print(slownik)
