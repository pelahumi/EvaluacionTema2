#Creamos la clase alumno
class Alumno():

    #Creamos el constructor
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    print("El alumno se ha creado con éxito.")
    
    #Creamos el método de calificación
    def calificacion(self):
        if 5 <= self.nota <= 10:
            print("Has aprobado")
        elif 0 <= self.nota <5:
            print("Has suspendido")
        else:
            print("La nota introducida no está dentro de los parámetros")


alumno1 = Alumno("Antonio", 4)
alumno2 = Alumno("Pablo", 9)

alumno1.calificacion()
alumno2.calificacion()

