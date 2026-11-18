def mostrar_estadisticas(paises):

    if len(paises) == 0:
        print("No hay datos para calcular estadisticas.")
        return

    mayor = paises[0]
    menor = paises[0]

    total_poblacion = 0
    total_superficie = 0

    continentes = {}

    for pais in paises:

        total_poblacion += pais["poblacion"]
        total_superficie += pais["superficie"]

        if pais["poblacion"] > mayor["poblacion"]:
            mayor = pais

        if pais["poblacion"] < menor["poblacion"]:
            menor = pais

        continente = pais["continente"]

        if continente in continentes:
            continentes[continente] += 1
        else:
            continentes[continente] = 1

    promedio_poblacion = total_poblacion / len(paises)
    promedio_superficie = total_superficie / len(paises)

    print("==== ESTADISTICAS ====")

    print(f"Pais mas poblado: {mayor["nombre"]}")
    print(f"Pais menos poblado: {menor["nombre"]}")

    print(f"Promedio de poblacion: {round(promedio_poblacion, 2)}")
    print(f"Promedio de superficie: {round(promedio_superficie, 2)}")

    print("Cantidad de paises por continente:")

    for continente, cantidad in continentes.items():
        print(continente, ":", cantidad)
