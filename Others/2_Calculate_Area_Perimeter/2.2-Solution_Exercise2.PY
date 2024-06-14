# Importacion de la biblioteca math para poder usar el metodo pi
from math import pi
from modulo import figura_geometrica, calculo_geometrico


def mi_funcion():
    while True:
        figure = figura_geometrica()

        print("Ahora, escogeremos uno de los dos tipos de calculos para la figura que escogiste: \n A para hallar el area \n P para hallar el perimetro")

        Calculate = calculo_geometrico()

        # Calculo de area y perimetro para el cuadrado
        if figure == "C" and Calculate == "A":
            lado_C = float(
                input("Por favor, dame el valor del lado del cuadrado: "))
            areaCuadrado = (pow(lado_C, 2))
            print("El area de tu cuadrado es: " + " " + str(areaCuadrado))

        elif figure == "C" and Calculate == "P":
            lado_C = float(
                input("Por favor, dame el valor del lado del cuadrado: "))
            perimetroCuadrado = (lado_C * 4)
            print("EL perimero de tu cuadrado es: " + str(perimetroCuadrado))

        # Calculo de area y perimetro para el circulo
        if figure == "O" and Calculate == "A":
            radio = float(input("por favor, digita el radio de tu circulo: "))
            areaCirculo = (pi * pow(radio, 2))
            print("El area de tu circulo es: " + str(areaCirculo))

        elif figure == "O" and Calculate == "P":
            radio = float(input("por favor, digita el radio de tu circulo: "))
            perimetroCirculo = (2 * pi * radio)
            print("EL perimetro de tu circulo es:  " + str(perimetroCirculo))

            # Caclculo de area y perimetro para el rectangulo
        if figure == "R" and Calculate == "A":
            base_R = float(
                input("Digita el valor de la base de tu rectangulo: "))
            altura_R = float(
                input("Digita el valor de la altura de tu rectangulo: "))
            areaRectangulo = (base_R * altura_R)
            print("El area de tu rectangulo es: " + str(areaRectangulo))

        elif figure == "R" and Calculate == "P":
            base_R = float(
                input("Digita el valor de la base de tu rectangulo: "))
            altura_R = float(
                input("Digita el valor de la altura de tu rectangulo: "))
            perimetroRectangulo = ((base_R * 2) + (altura_R * 2))
            print("El perimetro de tu rectangulo es: " + str(perimetroRectangulo))

            # Calculo de area y perimetro para el triangulo
        if figure == "T" and Calculate == "A":
            base_T = float(
                input("Digita el valor de la base de tu triangulo: "))
            altura_T = float(
                input("Digita el valor de la altura de tu triangulo: "))
            areaTriangulo = ((base_T * altura_T) / 2)
            print("El area de tu triangulo es: " + str(areaTriangulo))

        elif figure == "T" and Calculate == "P":
            lado_T = float(input("ingresa el valor de lado de tu triangulo: "))
            perimetroTriangulo = (lado_T * 3)
            print("El perimetro de tu triangulo es : " + str(perimetroTriangulo))

        # Verificacion de reiniciar el programa
        if True:
            Desicion = input(
                "Si deseas realizar otra operacion, digita S. \n Si quieres salir del programa, presiona cualquier tecla: ").upper()

            if Desicion != "S":
                break


mi_funcion()
