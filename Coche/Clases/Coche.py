import Vehiculo

class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada): 
        super().__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    print("Coche creado con éxito.")

def __str__(self):
    return "color {}, {} km/h, {} ruedas, {} cc".format(self.color, self.velocidad, self.ruedas, self.cilindrada )

coche = Coche("azul", 150, 4, 1200)
print(coche.__str__())