# suspenso

lista1= ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua" ]
lista2= []
susp=[]

for i in range(len(lista1)): 
    nota= int(input("Introduce la nota de la asignatura "+lista1[i]))
    lista2.append(nota)
    
    if nota < 5:
        susp.append(lista1[i])
print("Tienes que repetir la asignatura", susp)