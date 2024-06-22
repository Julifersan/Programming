# Escribir un programa que lea un entero positivo, n  introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:

# suma = (n(n+1))/2

def suma():
    n = int(input("ingrese un numero entero: "))

    for i in range(1, n+1):
        operacion = (i*(i+1))/2
        print("El primer resultado es: ", operacion)


suma()
