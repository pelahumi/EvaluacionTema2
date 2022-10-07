def error1():
    a = 7/0
    try:
        print(a)
    except:
        ZeroDivisionError("No se puede dividir por cero.")
    else:
        print("Todo correcto.")

error1()
    
    