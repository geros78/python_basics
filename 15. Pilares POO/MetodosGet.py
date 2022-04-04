#El metodo get esta para obtener su valor, no modificarlo

class A():
    def __init__(self):
        self._cuenta =0
        self._contador =0

    @property                   # property permite llamar al metodo como atributo
    def cuenta(self):           #Metodo get
        return self._cuenta

    @property
    def contador(self):
        return self._contador

a = A()
print(a.cuenta)
print(a.contador)