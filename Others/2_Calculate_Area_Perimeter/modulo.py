def figura_geometrica():

    print("Por favor, mira las opciones que tiene el programa sobre las figuras geometricas que admite, para su posterior calculo de area y perimetro.")

    print("Digita:\n C para cuadrado \n R para rectangulo \n T para triangulo \n O para circulo")

    while True:
        figure = input(
            "Ingresa la figura geometrica que te interesa: ").upper()

        # Validacion de la longitud de caractere
        if len(figure) != 1:
            print("Por favor, digite una de las opciones validas para continuar el proceso: \n C para cuadrado \n R para rectangulo \n T para triangulo \n O para circulo")
            continue

            # Validacion de que sea un vaor alfabetico
        if not figure.isalpha():
            print("Por favor, digita un caracter que este dentro de las opciones correspondiente: \n C para cuadrado \n R para rectangulo \n T para triangulo \n O para circulo")

            # Validacion del tipo de figura geometrica
        elif figure == "O":
            print(
                "Genial, escogiste la figura del circulo, continuemos con tu siguiente eleccion.")
            break

        elif figure == "R":
            print(
                "Genial, escogiste la figura del rectangulo,  continuemos con tu siguiente eleccion.")
            break

        elif figure == "T":
            print(
                "Genial, escogiste la figura del triangulo,  continuemos con tu siguiente eleccion.")
            break

        elif figure == "C":
            print(
                "Genial, escogiste la figura del cuadrado,  continuemos con tu siguiente eleccion.")
            break

        else:
            print("Por favor, escoge una de las opciones validas del programa: \n C para cuadrado \n R para rectangulo \n T para triangulo \n O para circulo")

    return figure


def calculo_geometrico():
    while True:
        Calculate = input(
            "Escribe el tipo de calculo que deseas realizar: ").upper()

        # Validacion de la longitud
        if len(Calculate) != 1:
            print("Por favor, digita una de las dos opciones correspondientes: \n A para hallar el area \n P para hallar el perimetro.")
            continue

        if not Calculate.isalpha():
            print("Por favor, digita una opcion valida para poder continuar: \n A para hallar el area \n P para hallar el perimetro.")

        elif Calculate == "A":
            print("Escogiste area, muy buena eleccion, sigamos.")
            break

        elif Calculate == "P":
            print("Escogiste perimetro, muy buena eleccion, sigamos.")
            break

        else:
            print("Me gusta que intentes ser crtic@, pero escoge una opcion: \n A para hallar el area \n P para hallar el perimetro.")

    return Calculate
