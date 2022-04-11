class vehiculo:
    def __init__(self,marca,matricula,color):
        self.marca=marca
        self.matricula = matricula
        self.color = color

class automovil(vehiculo):
    def __init__(self,numPuertas,modelo):
        vehiculo.__init__(self,"mazda","AAA111",",mazda6")
        self.numPuertas=numPuertas
        self.modelo=modelo

class motocicleta(vehiculo):
    def __init__(self,modelo):
        vehiculo.__init__(self,"harley-davidson","BBB222","clasicc")
              
