class A():
    def __init__(self):
        self._contador = 0  #los atributos se encapsulan con (_)
    
    def incrementar (self):
        self._contador += 1
    
    def cuenta (self):
        return self._contador

a = A()
# print(a.cuenta)
# a.cuenta + 20      Estas son malas practicas al cambiar atributos o llamarlos
# print (a.cuenta)

 