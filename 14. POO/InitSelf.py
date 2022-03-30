'''class FabricaTelefonos():
    marca = "Samsung"

    def elaborarHuawei(self):   #self Permite englobar un argumento a toda la clase   
       self.marca = "Huawei"

telefono = FabricaTelefonos()
telefono.elaborarHuawei()
print(telefono.marca)'''

class FabricaTelefonos():

    #__init__ ejecuta siempre que se manda a llamar un ojeto

    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

telefono = FabricaTelefonos('Huawei', 'Negro')
print(telefono.marca)
print(telefono.color)

