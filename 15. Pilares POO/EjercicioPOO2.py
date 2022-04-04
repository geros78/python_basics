class Operaciones():
    def __init__(self):
        self.num1 = int(input("Ingrese el Primer Valor: "))
        self.num2 = int(input("Ingrese el Segundo Valor: "))

    def suma(self):
        self.suma = self.num1 + self.num2
        print ("La suma es: ", self.suma)
    
    def resta(self):
        self.resta = self.num1 - self.num2
        print ("La resta es: ", self.resta)

    def multi(self):
        self.multi = self.num1 * self.num2
        print ("La multiplicacion es: ", self.multi)

    def div(self):
        self.div = self.num1 / self.num2
        print ("La division es: ", self.div)

calcular = Operaciones()
calcular.suma()
calcular.resta()
calcular.multi()
calcular.div()