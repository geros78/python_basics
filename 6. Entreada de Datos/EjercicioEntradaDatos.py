from math import sqrt

#Punto1

a = int(input("Digite valor a: "))
b = int(input("Digite valor b: "))
c = int(input("Digite valor c: "))

#Solucion sin funcion sqrt

'''x1 = (-b + ((b**2) - (4*a*c))**0.5)/(2*a)
x2 = (-b - ((b**2) - (4*a*c))**0.5)/(2*a)'''


if((b**2)-(4*a*c))< 0 :
    print ("No se puede realizar porque es un numero negativo")
else:
    x1 = (-b + sqrt((b**2) - (4*a*c)))/(2*a)
    x2 = (-b - sqrt((b**2) - (4*a*c)))/(2*a)

print("Solucion en x1: ", x1, "\n Solucion en x2: ",x2)


#Punto2

practica1 = float(input("Nota practica 1: "))
practica2 = float(input("Nota practica 2: "))
practica3 = float(input("Nota practica 3: "))

examenParcial = float(input("Nota examen parcial: "))
examenFinal = float(input("Nota examen final: ")) 

pp= (practica1+practica2+practica3)/3

prom = (pp + 2*examenParcial + 3*examenFinal)/6

print("El promedio es: ", prom)