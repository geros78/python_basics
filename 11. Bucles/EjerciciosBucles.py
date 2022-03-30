#punto1 

print("Ejercicio 1: \n")

for k in range(1, 10+1):
    print(k)

#-----------------------------------------------

listaNum = []

inicio = int(input("Ingrese el rango inicial: "))
fin = int(input("Ingrese el rango final: "))

for i in range(inicio, fin+1):
    listaNum.append(i)

print(listaNum)

#------------------------------------------------

#Punto2

listaNum2 = []

print("\nEjercicio 2:")

inicio2 = int(input("Ingrese el rango inicial: "))
fin2 = int(input("Ingrese el rango final: "))

for i in range(inicio2, fin2+1):
    if i%2 !=0:
        listaNum2.append(i)
        
print(listaNum)        