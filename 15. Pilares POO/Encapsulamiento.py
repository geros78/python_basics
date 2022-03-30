class A():
    def __init__(self):
        self.contador = 0

    def incremetar(self):
        self.contador += 1

    def cuenta(self):
        return self.contador

class B():
    def __init__(self):
        self.__contador = 0

    def incremetar(self):
        self.__contador += 1

    def cuenta(self):
        return self.__contador

print('Objeto 1')

a = A()
print(a.cuenta())
a.incremetar()
print(a.cuenta())
print(a.contador)

print('Objeto 2')

b =B()
print(b.cuenta())
b.incremetar()
print(b.cuenta())
print(b.__contador)

# El encapsulamiento es un atributo hecho para que 
# solo pueda ser usado dentro de la misma clase