class FabricaTelefonos():
    def __init__(self, marca, *colores, **modelos):
        self.marca = marca
        self.colores = colores
        self.modelos = modelos

telefono = FabricaTelefonos("Alcatel", "Negro", "Azul", m1 = 500, m2 = 2)
print(telefono.marca)
print(telefono.colores)
print(telefono.modelos)

#Crear un atributo temporal

telefono.memoria = 512
print(telefono.memoria)