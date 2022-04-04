class Estudiante():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir (self):
        print("Nombre: {} \n Nota: {}".format (self.nombre, self.nota))

    def resultados(self):
        if self.nota < 7:
            print("Has reprobado")
        else:
            print("Has aprobado")
            

estudiante1 = Estudiante("Daniel", 10)
estudiante1.imprimir()
estudiante1.resultados()

estudiante2 = Estudiante("Andres", 5)
estudiante2.imprimir()
estudiante2.resultados()