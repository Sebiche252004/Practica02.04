#yo estudio

asignatura= input("Introduce las asignaturas que estudias separao por espacios")
lista= asignatura.split(",")
N = len(lista)
print(lista)
for i in range(N):
    print("Yo estudio", lista[i])
    