#palindromo

palabra= input("Introduzca una palabra para comprobar")
lista=list(palabra)
if lista == lista[::-1]:
    print("Tu palabra si es un palindromo")
else:
    print("Tu palabra no es un palindromo")