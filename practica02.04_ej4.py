# loteria 

lista = []
totales= int(input("Introduce el numero totales de tu loteria"))

for i in range (totales):
    numero= int(input("Introduce numeros de la loteria"))
    lista.append(numero)
lista.sort()
print(lista)
    