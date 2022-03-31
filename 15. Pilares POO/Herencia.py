#La Herencia permite a una clase hija usar los meotodos de una clase padre

class Animales():       #Clase padre
    def habla(self):
        print("Yo soy un animal")

    def description(self):
        print("Yo soy una {}".format (self.animal))

class Perro(Animales): #Clase hija
    pass

class Abeja(Animales):
    def __init__(self, animal):
        self.animal =animal
    pass

# La clase Perro y Abeja hereda de la clase Animales

animal = Animales()
animal.habla()

perro = Perro()
perro.habla()

abeja = Abeja("Abeja")
abeja.description()
