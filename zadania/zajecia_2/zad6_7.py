lista=list(range(1,11))
print(lista)

lista2=lista[5:] 
del lista[5:]
print(lista)
print(lista2)

lista3 = lista+lista2 
print(lista3)

lista3.insert(0,0) 
print(lista3)

lista3.sort(reverse=True) 
print(lista3)

