# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

horas_trabajadas = float(input("digite el número de horas que trabaja: "))

coste_hora = float(input("Ingrese el valor de tu hora de trabajo: "))

paga = coste_hora * horas_trabajadas

decimales = int(paga)

print(decimales)
