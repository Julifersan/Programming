# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

# Fórmula IMC = Peso (Kg) / Estatura al cuadrado (Mt). Ejemplo: Una persona pesa 64 Kg y mide 1.5 metros: 64 / 1.5 x 1.5 = 28.44.

peso = float(input("Digita tu peso en kg: "))
altura = float(input("Digita tu altura en metros: "))

imc = peso / pow(altura, 2)

print(f"Tu IMC es de: {imc}")
