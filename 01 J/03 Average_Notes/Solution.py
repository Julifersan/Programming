def promedio():
    while True:
        try:
            # Solicitud del valor de cada una de las notas del alumno
            Nota1 = float(input("Ingrese primera nota: "))
            Nota2 = float(input("Ingrese segunda nota: "))
            Nota3 = float(input("Ingrese tercera nota: "))

        except ValueError:
            print("Por favor, ingrese un valor numerico valido.")
            continue

        List_Notes = [Nota1, Nota2, Nota3]
        Average = sum(List_Notes) / len(List_Notes)

        if Average >= 7:
            print(f"Tu nota promedio es de {
                  Average}, lo cual obtienes la condicion de PROMOCIONADO :) ... ¡FELICIDADES!")

        elif Average >= 4:
            print(f"Tu nota promedio es de {
                  Average}, lo cual obtienes la condicion de REGULAR :| ... ¡PUEDES HACERLO MEJOR!  ")

        else:
            print(f"Tu nota promedio es de {
                  Average} REPROBADO :o ... ¡CONFIA EN TI, PERSEVERA Y LO LOGRARAS!")

        Desicion = input(
            "digita S para SALIR en la aplicacion y promediar otro alumno,  de lo contrario presiona cualquier tecla para CONTINUAR ").upper()

        if Desicion == "S":
            break


promedio()
