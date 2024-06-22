#BIENVENIDO AL MÓDULO PRINCIPAL, PUEDES PROBARLO


#Se importa el método pi del módulo math
from math import pi

#Se importa el módulo para realizar los cálculos
import FG_tipo_figura_calculo as cal

def calculo2D():
    while True:
        cal.Tipofigura
        cal.Tipocalculo

        figure = cal.Tipofigura()
        calculate = cal.Tipocalculo()

        # Cálculo de área y perímetro para el cuadrado
        if figure == "C":
            if calculate == "A":
                Lado_C = input("Digita el valor númerico de uno de los LADOS del CUADRADO:\n        ➡️  :")
                try:
                    Lado_C = float(Lado_C)
                except NameError:
                    print("Por favor, digita un valor NÚMERICO 🔢\n\n")
                    continue

                area = (pow(Lado_C, 2))
                return area

            elif calculate == "P":
                Lado_C = input("Digita el valor númerico de uno de los LADOS del CUADRADO:\n        ➡️  :")
                try:
                    Lado_C = float(Lado_C)
                except NameError:
                    print("Por favor, digita un valor NÚMERICO 🔢\n\n")
                    continue

                perimetro = (Lado_C * 4)
                return perimetro


        # Cálculo de área y perímetro para el círculo
        if figure == "O":
            if calculate == "A":
                Radio = input("Digita el valor númerico del RADIO del CÍRCULO:\n        ➡️  :")
                try:
                    Radio = float(Radio)
                except NameError:
                    print("Por favor, digita un valor NÚMERICO 🔢\n\n")
                    continue

                area = (pi * pow(Radio, 2))
                return area

            elif calculate == "P":
                Radio = input("Digita el valor númerico del RADIO del CÍRCULO:\n        ➡️  :")
                try:
                    Radio = float(Radio)
                except NameError:
                    print("Por favor, digita un valor NÚMERICO 🔢\n\n")
                    continue
                perimetro = (2 * pi * Radio)
                return perimetro
           


        # Cálculo de área y perímetro para el rectángulo
        if figure == "R":
            if calculate == "A":
                Lado_pequeño = input("Digita el valor númerico del LADO más pequeño del RECTÁNGULO:\n        ➡️  :")
                try:
                    Lado_pequeño = float(Lado_pequeño)
                except NameError:
                    print("Por favor, digita un valor NÚMERICO 🔢\n\n")
                    continue
                Lado_grande = input("Ahora digita el valor númerico del LADO más grande del RECTÁNGULO:\n        ➡️  :")
                try:
                    Lado_grande = float(Lado_grande)
                except NameError:
                    print("Por favor, digita un valor NÚMERICO 🔢\n\n")
                    continue

                area = (Lado_pequeño * Lado_grande)
                return area

            elif calculate == "P":
                Lado_pequeño = input("Digita el valor númerico del LADO más pequeño del RECTÁNGULO:\n        ➡️  :")
                try:
                    Lado_pequeño = float(Lado_pequeño)
                except NameError:
                    print("Por favor, digita un valor NÚMERICO 🔢\n\n")
                    continue
                Lado_grande = input("Ahora Digita el valor númerico del LADO más grande del RECTÁNGULO:\n        ➡️  :")
                try:
                    Lado_grande = float(Lado_grande)
                except NameError:
                    print("Por favor, digita un valor NÚMERICO 🔢\n\n")
                    continue

                perimetro = ((Lado_pequeño * 2) + (Lado_grande * 2))
 
                return perimetro

        # Cálculo de área y perímetro para el triángulo
        if figure == "T":
            if calculate == "A":
                Base_T = input("Digita el valor númerico de la BASE del TRIÁNGULO EQUILÁTERO:\n        ➡️  :")
                try:
                    Base_T = float(Base_T)
                except NameError:
                    print("Por favor, digita un valor NÚMERICO 🔢\n\n")
                    continue
                Altura_T = input("Ahora Digita el valor númerico de la ALTURA del TRIÁNGULO EQUILÁTERO:\n        ➡️  :")
                try:
                    Altura_T = float(Altura_T)
                except NameError:
                    print("Por favor, digita un valor NÚMERICO 🔢\n\n")
                    continue

                area = ((Base_T * Altura_T) / 2)
                return area

            elif calculate == "P":
                Base_T = input("Digita el valor númerico de la BASE del TRIÁNGULO EQUILÁTERO:\n        ➡️  :")
                try:
                    Base_T = float(Base_T)
                except NameError:
                    print("Por favor, digita un valor NÚMERICO 🔢\n\n")
                    continue

                perimetro = (Base_T * 3)
                return perimetro

resultado = calculo2D()

print(f"EL resultado de tu cálculo tuvo un valor de {resultado} unidades\n\n")

