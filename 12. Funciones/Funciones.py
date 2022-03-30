#Plantilla de una funcion

def saludo():
    print("Hola")

saludo(), saludo(), saludo()

mul = int(input("Tabla de multiplicacion: "))

def tablaMultiplicacion():
    for i in range(10+1):
        print("{} x {} = {}".format(mul ,i, i*mul))

tablaMultiplicacion()