# Se importa la libreria random para generar una aleatoreidad en las palabras
import random

# Se importa csv para generar un nuevo archivo con este tipo
import csv


def anagrama():
    # Se crea el archivo anagrama con extension csv, en donde esta en modo escritura y el newline, significa que se pase a una nueva línea apenas termine de escribir los registros de los encabezados, los cuales estarán definidos más adelante
    # La variable "escribir" define el metodo csv.writer con el parámetro file, que es mi archivo.

    with open("anagrama.csv", mode="w", newline="") as archivo:
        escribir = csv.writer(archivo)

        # Se definen los atributos o columnas que perteneceran a la entidad anagrama.csv
        escribir.writerow(["ID", "Palabra1", "Anagrama1",
                          "Palabra2", "Anagrama2", "Estado"])

        # Se define el inicio del registro del con un ID único
        id_counter = 1

        # Se inicia un bucle infinito para generar los datos a partir de la interaccion del usuario con el programa
        while True:
            # Se solicita al usuario dos palabras por separado
            Palabra1 = input("Por favor, escribe una palabra: ").upper()
            Palabra2 = input("Por favor, escribe la segunda palabra: ").upper()

            # Cada palabra se convierte en una ista, siendo los carácteres los elementos de la misma lista
            P1 = list(Palabra1)
            P2 = list(Palabra2)

            # Se barajan o revuelven los elementos de cada lista
            random.shuffle(P1)
            random.shuffle(P2)

            # Se guarda en un string el resultado de barajar las listas en un string
            resul1 = "".join(P1)
            resul2 = "".join(P2)

            # Se establece una condición para "verificar si es o no un anágrama"
            if sorted(Palabra1) == sorted(Palabra2):
                print(
                    "No es un anagrama. Por favor, ingresa dos palabras distintas entre sí.")
                Status = False
                continue
            else:
                print("Es un anagrama.")
                Status = True

            # Se muestra por concola el resultado de barajar las palabras
            print(f"La palabra {Palabra1} barajada es: {resul1}")
            print(f"La palabra {Palabra2} barajada es: {resul2}")

            # Se genera un nuevo registro(Fila), en el archivo csv
            escribir.writerow(
                [id_counter, Palabra1, resul1, Palabra2, resul2, Status])

            # Se pregunta al usuario si desea seguir usando el programa
            decision = input(
                "Si deseas salir de la aplicación, escribe 'S'; de lo contrario, oprime cualquier tecla: ").upper()
            if decision == "S":
                print("Gracias por utilizar el programa.")
                break
            else:
                # Se le suma 1 a cada iteración del programa
                id_counter += 1


anagrama()
