class Vehiculo():

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
        

def __str__(self):
    
    return "Color {}, {} ruedas".format( self.color, self.ruedas )



class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada): 
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    print("Coche creado con éxito.")

def __str__(self):
    return "color {}, {} km/h, {} ruedas, {} cc".format(self.color, self.velocidad, self.ruedas, self.cilindrada )

coche = Coche("azul", 150, 4, 1200)
print(coche.__str__())