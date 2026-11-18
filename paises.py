def agregar_pais(paises):
    print("--- AGREGAR PAIS ---")

    nombre = input("Nombre: ").strip()

    if nombre == "":
        print("El nombre no puede estar vacio.")
        return

    # Comprobar que no exista
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            print("Ese pais ya existe.")
            return

    continente = input("Continente: ").strip()

    if continente == "":
        print("El continente no puede estar vacio.")
        return

    poblacion_texto = input("Poblacion: ").strip()
    superficie_texto = input("Superficie en km2: ").strip()

    if not poblacion_texto.isdigit() or not superficie_texto.isdigit():
        print("Debes ingresar numeros enteros.")
        return

    poblacion = int(poblacion_texto)
    superficie = int(superficie_texto)

    if poblacion <= 0 or superficie <= 0:
        print("Los valores deben ser mayores a cero.")
        return

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(nuevo_pais)

    print("Pais agregado correctamente.")


def buscar_pais(paises):
    nombre = input("Ingrese el nombre del pais: ").strip().lower()

    if nombre == "":
        print("Debe ingresar un nombre para buscar.")
        return
    
    encontrados = []

    for pais in paises:
        if nombre in pais["nombre"].lower():
            encontrados.append(pais)

    if len(encontrados) == 0:
        print("No se encontraron resultados.")
    else:
        for pais in encontrados:
            mostrar_pais(pais)


def mostrar_pais(pais):
    print("------------------------------")
    print("Nombre:", pais["nombre"])
    print("Poblacion:", pais["poblacion"])
    print("Superficie:", pais["superficie"], "km2")
    print("Continente:", pais["continente"])


def actualizar_pais(paises):
    nombre = input("Pais a actualizar: ").strip().lower()

    for pais in paises:
        if pais["nombre"].lower() == nombre:

            print("Pais encontrado:", pais["nombre"])
            print("Deje vacio un campo para conservar su valor.")

            nueva_poblacion = input("Nueva poblacion: ").strip()
            nueva_superficie = input("Nueva superficie: ").strip()

            if nueva_poblacion != "":
                if not nueva_poblacion.isdigit() or int(nueva_poblacion) <= 0:
                    print("Poblacion invalida.")
                    return

            if nueva_superficie != "":
                if not nueva_superficie.isdigit() or int(nueva_superficie) <= 0:
                    print("Superficie invalida.")
                    return

            if nueva_poblacion == "" and nueva_superficie == "":
                print("No se ingresaron cambios.")
                return

            # Finalmente aplicamos las modificaciones
            if nueva_poblacion != "":
                pais["poblacion"] = int(nueva_poblacion)

            if nueva_superficie != "":
                pais["superficie"] = int(nueva_superficie)

            print("Datos actualizados correctamente.")
            return

    print("No se encontro el pais.")


def filtrar_continente(paises):
    continente = input("Ingrese el continente: ").strip().lower()

    resultados = []

    for pais in paises:
        if pais["continente"].lower() == continente:
            resultados.append(pais)

    mostrar_resultados(resultados)


def filtrar_rango(paises, campo):
    print("\nIngrese el rango deseado.")

    minimo_texto = input("Valor minimo: ").strip()
    maximo_texto = input("Valor maximo: ").strip()

    if not minimo_texto.isdigit() or not maximo_texto.isdigit():
        print("Debe ingresar numeros enteros.")
        return

    minimo = int(minimo_texto)
    maximo = int(maximo_texto)

    if minimo > maximo:
        print("El minimo no puede superar al maximo.")
        return

    resultados = []

    for pais in paises:
        valor = pais[campo]

        if minimo <= valor <= maximo:
            resultados.append(pais)

    mostrar_resultados(resultados)


def ordenar_paises(paises, campo, descendente=False):
    ordenados = sorted(
        paises,
        key=lambda pais: pais[campo].lower() if campo == "nombre" else pais[campo],
        reverse=descendente
    )

    mostrar_resultados(ordenados)

def mostrar_resultados(resultados):
    if len(resultados) == 0:
        print("No se encontraron paises.")
        return

    for pais in resultados:
        mostrar_pais(pais)
