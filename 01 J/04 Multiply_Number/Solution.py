def number():

    while True:
        try:
            Numerito = float(input("Ingrese tu número: "))
        except ValueError:
            print("Por favor, ingrese un valor numerico")
            continue

        for i in range(1, 101):
            print(f"Tu numero por {i} es igual a: {Numerito * i}")

        Desicion = input(
            "Si deseas SALIR  presiona S, de lo contrario, presiona cualquier tecla para que continues con otro numero ").upper()

        if Desicion == "S":
            break


number()
