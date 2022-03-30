#Punto 1

palabra1 = input("Escriba una palabra: ")
palabra2 = input("Escriba una palabra que rime: ")

if len(palabra1) < 3 or len(palabra2) <3:
    print("No rima, porque tiene menos de 3 caracteres")
elif palabra1[-3:] == palabra2[-3:]:
    print("Las palabras riman")
elif palabra1[-2:] == palabra2[-2:]:
    print("Las palabras riman un poco")
else:
    print("Las palabras no riman")

#Punto 2
candidato = input('Elija una candidato\n Los candidatos son: "A", "B", "C" ')

if candidato.upper() == "A":
    print("Usted ha votado por el partido rojo")
elif candidato.upper() == "B":
    print("Usted ha votado por el partido verde")
elif candidato.upper() == "C":
    print("Usted ha votado por el partido azul")
else:
    print("Opcion erronea")