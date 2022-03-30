#punto1 

print("\n punto1 \n")

lista = [20, 50, "Curso", 'Python', 3.14]

print("Valores actuales: ", lista)

valor1 = input("agrega el primer valor: ")
valor2 = input("agrega el segundo valor: ")

lista[0] = valor1
lista[1] = valor2

print("Valores finales: ", lista)

#punto2

print("\n punto2 \n")

lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Valores iniciales: ", lista2)


lista2[3] *= 2
lista2[6] *= 2 
lista2[8] *= 2
print("Valores finales: ", lista2)