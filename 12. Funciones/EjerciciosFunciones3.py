def mayorMenorIgual ():
    num1 = int(input("Ingrese primer numero: "))
    num2 = int(input("Ingrese segundo numero: "))

    if num1 > num2:
        return 1
    elif num1 < num2:
        return -1
    else:
        return 0



def valorIva (iva):
    valor = int(input("Valor del producto: "))

    if iva == 0:
        porcentaje = valor *0.21
        valorIva = valor + porcentaje

        return print("Valor del producto: {}\nValor del IVA: {} \nValor con IVA: {}".format(valor, porcentaje, valorIva))
    elif iva < 0:

        return print("Valor del IVA no puede ser negativo")
    
    else:
        porcentaje = valor *iva
        valorIva = valor + porcentaje

        return print("Valor del producto: {}\nValor del IVA: {} \nValor con IVA: {}".format(valor, porcentaje, valorIva))
    

print(valorIva(0.21))
