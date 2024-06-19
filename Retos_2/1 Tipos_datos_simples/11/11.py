# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

# interes de 4% al año
interes = 0.4

monto = float(input("Digita el monto que se depositó en la cuenta bancaria: "))

g1 = interes * monto
g1_1 = round(g1, 2)

g2 = (interes*2) * monto
g2_2 = round(g2, 2)

g3 = (interes*3) * monto
g3_3 = round(g3, 2)

print(f"Cantidad de ahorro en el primer año fue de {g1_1}")
print(f"Cantidad de ahorro en el segundo año fue de {g2_2}")
print(f"Cantidad de ahorro en el tercer año fue de {g3_3}")
