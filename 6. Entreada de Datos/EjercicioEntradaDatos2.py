#Punto1

vocal = input("Escribe una vocal: ")
letra = input("Escribe una letra: ")

if vocal in "aeiou":
    print("Vocal en mayuscula: ",vocal.upper())
else:
    print("No es una vocal")

print("Letra en minuscula: ",letra.lower())

#Punto2

nombre = input("Escribe tu nombre: ")
edad = input("Escribe tu edad: ")
sexo = input("Escribe tu sexo: ")

print("Te llamas: {} \nTu edad es: {} \nEres: {}".format(nombre,edad,sexo))