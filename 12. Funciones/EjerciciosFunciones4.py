
def areaCuadrada (base, altura):
    area = base *altura
    return area

base = int(input("Base: "))
altura = int(input("Altura: "))

print(areaCuadrada(base, altura))



def circunferencia (radio):
    global pi
    pi = 3.14
    circu = pi *(radio**2)
    return circu

radio = int(input("radio: "))


print(circunferencia(radio))


def media(*tupla):
    for i in tupla:
        print(i)
    return (len(tupla))

print(media(5,5,5))