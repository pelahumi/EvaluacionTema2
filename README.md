# EvaluacionTema2

[Link del repositorio](https://github.com/pelahumi/EvaluacionTema2)

## Ejercicio 1:
En este ejercicio creamos la clase Alumno con su constructor y añadimos el método calificación, que calificará al alumno en función de si su nota es mayor a 5 o no.

```
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
```

## Ejercicio 2:
En este ejercicio añadimos a la clase str que muestra los datos de cada alumno.

```
    #Creamos el método str
    def __str__(self):
        return f"{self.nombre}: {self.nota}"
```        
    
    
---

La clase quedaría de esta forma:

```
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

