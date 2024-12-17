#  abecedario

lista= ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
lista2= []
N= len(lista)

for i in range(0,N,3):
    lista2.append(lista[i])
for i in range(1,N,3):
    lista2.append(lista[i])
    
lista2.sort()
print(lista2)