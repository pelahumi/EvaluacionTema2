#Creamos la clase alumno
class Alumno():

    #Creamos el constructor
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print("El alumno se ha creado con éxito.")