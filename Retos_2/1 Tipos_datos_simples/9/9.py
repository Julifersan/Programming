# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

# Ejemplos de tasas de interes:

inversion = float(input("Digite el monto a invertir: "))
interes = float(input("Digite la tasa de interes anual: "))
años = int(
    input("Digite lo años que piensa dejar el dinero produciendo para vos: "))

# La tasa de interés en una inversión es la cantidad de dinero que el inversionista recibe por cada periodo de tiempo global de su inversión.

ganancia_anual = inversion * interes
ganancia_total = ganancia_anual * años

print(f"vos, tendrías una retribución total de {
      ganancia_total}, por tu inversion de {inversion}")
