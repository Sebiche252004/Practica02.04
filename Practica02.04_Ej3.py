#notas

asignatura= input("Introduzca las asignaturas")
notas= input("Introduzca las notas sacadas")

lista1= asignatura.split(",")
lista2=notas.split(",")
N= len(lista1)
for i in range(N):
    print("En la asignatura", lista1[i], "has sacado", lista2[i])

