lista= []
numPar = []
numImp = []

def agregarNumeros():
    for i in range (10):
        num = int(input("Ingrese un numero a la lista: "))
        lista.append(num)

def organizarNumero():
    lista.sort()
    for j in lista:
        if j %2 == 0: 
           numPar.append(j)
        else:
            numImp.append(j)
    


agregarNumeros()

print(lista)

organizarNumero()

print("Lista par: ", numPar)
print("Lista impar: ", numImp)