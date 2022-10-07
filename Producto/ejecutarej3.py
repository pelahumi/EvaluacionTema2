import Producto.Clases.Ejercicio3

def ejecutar2():
    while True:

        print("========================") 
        print(" BIENVENIDO A Los ejercicios 1 y 2 ") 
        print("========================") 
        print("[1] Ejercicio 3 ")  
        print("[2] Cerrar el Manager ")
        print("========================")

        opcion = input("> ")

        if opcion == 1:

            print("Ejercicio 3...")
            print("Vamos a crear un producto: ", "\n")
            codigo = int(input("Introduce el codigo del producto: "))
            nombre = str(input("Introduce el nombre del producto: "))
            precio = int(input("Introduce el precio del producto: "))
            tipo = str(input("Introduce el tipo del producto: "))

            producto = Producto.Clases(codigo, nombre, precio, tipo)
            
            print("Veamos si el metodo str funciona: ", "\n")

            producto.__str__()
            break
        
        if opcion == 2:
            print("Cerrando el programa...")
            break

