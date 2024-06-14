def numeroprimo():
    for i in range(1, 101):
        ome = i
        if ome % 2 == 0 and ome % 1 == 0:
            if ome == 2:
                print("El numero 2 es un primo")
                continue
            print(f"El numero {ome} No es un numero primo")
        elif ome % 1 == 0 and ome % ome == 0:
            print(f"El numero {ome} es un primo")


numeroprimo()
