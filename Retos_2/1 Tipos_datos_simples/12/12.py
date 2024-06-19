# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

# Valor barra de pan individual en euros
pan = 3.49

# pan que no es del día descuento del 60%
descuento = 0.6

# Numero de barras vendidas que no son del día
pan_viejo = int(
    input("Digite el numero de panes vendidos que no son frescos: "))

coste = pan_viejo * pan
coste_con_descuento = coste * descuento

# Mostrar precio habitual de una barra de pan
print(f"El precio de una barra de pan fresca es de {pan} euros")
print("El descuento otorgado a una barra de pan que no es fresco es del 60%")
print(f"El valor total por las barras de pan que se vendieron fue de {
      coste_con_descuento} euros")
