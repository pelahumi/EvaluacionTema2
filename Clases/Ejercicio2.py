#Creamos la clase alumno
class Alumno():

    #Creamos el constructor
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print("El alumno se ha creado con éxito.")
    
    #Creamos el método str
    def __str__(self):
        return f"{self.nombre}: {self.nota}"
    
    #Creamos el método de calificación
    def calificacion(nota):
        nota = int(input("Introduce una nota del 0 al 10"))
        if 5 <= nota <= 10:
            print("Has aprobado")
        elif 0 <= nota <5:
            print("Has suspendido")
        else:
            print("La nota introducida no está dentro de los parámetros")
            
alumno1 = Alumno("Antonio", 4)
alumno2 = Alumno("Pablo", 9)

print(alumno1.__str__())
print(alumno2.__str__())
