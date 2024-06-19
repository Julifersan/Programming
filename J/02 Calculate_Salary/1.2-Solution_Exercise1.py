import csv

# Creamos la clase Datos como clase base


class Datos:
    def __init__(self, ph: float, hd: int, ds: int, semanas: int = 4):
        self.pago_por_hora = ph  # precio por hora trabajada
        self.horas_dia = hd  # horas trabajadas en un día promedio
        self.dias_semana = ds  # días laborados en una semana
        self.semanas = semanas  # 4 semanas tiene un mes

# Creamos la clase Operaciones, que hereda de Datos


class Operaciones(Datos):
    def sueldo(self):
        self.valor_dia = self.horas_dia * self.pago_por_hora
        self.valor_semana = self.dias_semana * self.valor_dia
        self.valor_mes = self.valor_semana * self.semanas

# Creamos la clase Resultados, que hereda de Operaciones


class Resultados(Operaciones):
    def dia(self):
        return f"Tu día laboral tiene {self.horas_dia} horas, con un coste de: ${self.valor_dia} mil COP"

    def semana(self):
        return f"Tu semana laboral tiene {self.dias_semana} días, con un coste de: ${self.valor_semana} mil COP"

    def mes(self):
        return f"Tu mes laborado tiene {self.semanas} semanas, con un coste de: ${self.valor_mes} mil COP"

# Creamos la función ingresos, que solicita datos y escribe en un archivo CSV


def ingresos():
    with open("ingresos.csv", mode="w", newline="") as file:
        escribir = csv.writer(file)

        escribir.writerow(["ID", "Trabajador", "Precio/Hora",
                          "HorasDiarias", "DiasSemana", "Valor/Dia", "Valor/Semana", "Valor/Mes"])

        idcount = 1

        while True:
            # Solicitud de datos
            nombre = input("Cuál es tu nombre: ")
            D1 = float(input("Ingrese el precio de tu hora laboral: "))
            D2 = int(input("Ingrese las horas que trabaja en un día: "))
            D3 = int(input("Ingrese los días que trabaja en una semana: "))

            # Creamos el objeto y llamamos a la clase Resultados
            trabajador = Resultados(D1, D2, D3)

            # Invocamos el método sueldo de la clase Operaciones
            trabajador.sueldo()

            print(trabajador.dia())
            print(trabajador.semana())
            print(trabajador.mes())

            escribir.writerow([idcount, nombre, D1, D2, D3, trabajador.valor_dia,
                              trabajador.valor_semana, trabajador.valor_mes])

            idcount += 1

            Desicion = input(
                "Si deseas salir de la aplicación, presiona 'S'.\nSi deseas realizar otro cálculo, presiona cualquier tecla: ").upper()

            if Desicion == "S":
                print("Gracias por usar el programa")
                break


# Llamamos a la función ingresos
ingresos()
