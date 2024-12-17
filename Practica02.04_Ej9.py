#vocal

palabra= input("Introduce una palabra cualquiera")
vocales= list("aeiou")
lista1=list(palabra)
a= lista1.count("a")
e=lista1.count("e")
i=lista1.count("i")
o=lista1.count("o")
u=lista1.count("u")
print("Tu palabra contiene la A",a,"veces",",", "la E", e,"veces",",", "la I", i,"veces",",", "la O", o,"veces","y","la U",u,"veces")