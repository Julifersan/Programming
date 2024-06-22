#ESTE ES EL MÓDULO DE COMPLEMENTO, POR FAVOR, SI QUIERES PROBAR EL CÓDIGO, INICIA CON EL OTRO MÓDULO


# Este módulo establece el tipo de figura y el tipo de cálculo, el cual tiene dos  métodos (Funciones), Tipofigura() y Tipocalculo()

#Se define la función Tipofigura(), la cual permite escoger el tipo de figura geométrica

#Triángulo Equilátero
def Tipofigura():
    while True:
        fig = input(
            "⬇️  Escoge la FIGURA GEOMÉTRICA de las opciones disponibles:\n\n    C: Para CUADRADO \n    R: Para RECTÁNGULO \n    T: Para TRIÁNGULO EQUILÁTERO\n    O: Para CÍRCULO\n\n        ➡️  :").upper()

        # Validacion de las opciones dadas
        if fig not in ["C", "R", "T", "O"]:
            print("😅 Por favor, digite una de las OPCIONES válidas para la FIGURA GEOMÉTRICA\n\n")
            continue

            # Validacion del tipo de figura geometrica
        elif fig == "C":
            figure = "C"
            print(
                "Genial, escogiste el CUADRADO.🦾\n")

        elif fig == "R":
            figure = "R"
            print(
                "Genial, escogiste el RECTÁNGULO.🦾\n")

        elif fig == "T":
            figure = "T"
            print(
                "Genial,escogiste el TRIÁNGULO EQUILÁTERO.🦾\n")

        elif fig == "O":
            figure = "O"
            print(
                "Genial, escogiste el CÍRCULO.🦾\n")

        return figure



# Función Tipocalculo(), la cual permite escoger el tipo de cálculo para la figura geométrica escogida en la función Tipofigura()
def Tipocalculo():
    while True:
        calculate = input(
            "⬇️  Ahora Escoge el tipo de CÁLCULO que deseas realizar.\n\nA: Para hallar el ÁREA\nP: Para hallar el PERÍMETRO ").upper()

        # Validacion de la longitud
        if calculate not in ["A", "P"]:
            print("😅 Por favor, digita una de las dos OPCIONES disponibles para CÁLCULO.")
            continue

        elif calculate == "A":
            C = "A"
            print("Super, Escogiste ÁREA.🎌\n")


        elif calculate == "P":
            C = "P"
            print("Super, Escogiste PERÍMETRO.🎌\n")
            
        return C
