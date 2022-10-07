from Alumno.ejecutarej1 import ejecutar1
from Producto.ejecutarej3 import ejecutar2

if __name__ == "__main__":
    
    while True:
        print("========================") 
        print(" BIENVENIDO AL MENÚ INICIAL ") 
        print("========================") 
        print("[1] Ejercicio 1 y 2 ") 
        print("[2] Ejercicio 3 ")
        print("[3] Ejercicio 4 ")
        print("[4] Ejercicio 5 ") 
        print("[5] Cerrar el Manager ")
        print("========================")

        opcion = int(input("> "))

        if opcion == 1:
            ejecutar1()
            break
            
        if opcion == 2:
            ejecutar2()
            break

        if opcion == 5:
            print("Cerrando el programa...")
            break