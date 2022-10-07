import Alumno.Clases.Ejercicio2

def ejecutar():
    while True:

        print("========================") 
        print(" BIENVENIDO A Los ejercicios 1 y 2 ") 
        print("========================") 
        print("[1] Ejercicio 1 ") 
        print("[2] Ejercicio 2 ") 
        print("[3] Cerrar el Manager ")
        print("========================")

        opcion = input("> ")

        if opcion == 1:

            print("Ejercicio 1...")
            print("Vamos a crear un alumno: ", "\n")
            nombre = str(input("Introduce el nombre del alumno: "))
            nota = int(input("Introduce la nota del alumno: "))

            alumno = Alumno.Clases(nombre, nota)
            
            print("Veamos si el alumno ha aprovado: ", "\n")

            alumno.calificacion()
            break

        if opcion == 2:

            print("Ejercicio 2...")
            print("Veamos si la función str funciona:", "\n")
            alumno.__str__()
            break
        
        if opcion == 3:
            print("Cerrando el programa...")
            break



