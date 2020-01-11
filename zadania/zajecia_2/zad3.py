c='{first} {last}'.format(first='przykladowy',last='tekst')
print(c)

d='{:=+5d}'.format(31) 
print(d)

dane = [10, 11, 12, 13, 14]  
e='{d[2]} {d[3]}'.format(d=dane)
print(e)

b='{:>10}'.format('tekst po prawej')
print(b)

a='{} {}'.format('przykladowy','tekst') 
print(a)




