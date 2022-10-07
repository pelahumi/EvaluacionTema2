from Coche.Clases.Vehiculo import *

def ejecutar3():
    print("Vamos a crear un coche: ")
    color = input("Introduce el color del coche: ")
    ruedas = input("Introduce el número de ruedas: ")
    velocidad = input("Introduce la velocidad máxima: ")
    cilindrada = input("Introduce la cilindrada: ")

    coche = Coche(color, ruedas, velocidad, cilindrada)
