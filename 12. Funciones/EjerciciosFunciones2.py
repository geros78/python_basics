
def factorializacion():
    num = int(input("Ingrese un numero: "))
    fac = 1
    for i in range(1, num+1):
        fac = fac*i
    print("Factorial de {} es igual a: {}".format(num, fac))

factorializacion()



