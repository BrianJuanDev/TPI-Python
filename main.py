from archivos import cargar_paises, guardar_paises
from paises import (
    agregar_pais,
    buscar_pais,
    actualizar_pais,
    filtrar_continente,
    filtrar_rango,
    ordenar_paises
)
from estadisticas import mostrar_estadisticas

def mostrar_menu():
    print("""
    =========================== 
        GESTION DE PAISES
    ===========================
    1. Agregar pais
    2. Actualizar pais
    3. Buscar pais
    4. Filtrar paises
    5. Ordenar paises
    6. Mostrar estadisticas
    0. Salir
    ===========================
    """)

def menu_filtros(paises):
    print(""" --- FILTROS --- 
    1. Por continente
    2. Por rango de poblacion
    3. Por rango de superficie
    """)

    opcion = input("Seleccione una opcion: ")

    match opcion:
        case "1":
            filtrar_continente(paises)

        case "2":
            filtrar_rango(paises, "poblacion")

        case "3":
            filtrar_rango(paises, "superficie")

        case _:
            print("Opcion invalida.")


def menu_ordenamientos(paises):
    print(""" 
    --- ORDENAMIENTOS ---
    1. Nombre (A-Z)
    2. Poblacion (menor a mayor)
    3. Poblacion (mayor a menor)
    4. Superficie (menor a mayor)
    5. Superficie (mayor a menor)
    """)

    opcion = input("Seleccione una opcion: ")

    match opcion:

        case "1":
            ordenar_paises(paises, "nombre")

        case "2":
            ordenar_paises(paises, "poblacion")

        case "3":
            ordenar_paises(paises, "poblacion", True)

        case "4":
            ordenar_paises(paises, "superficie")

        case "5":
            ordenar_paises(paises, "superficie", True)

        case _:
            print("Opcion invalida.")

def main():

    paises = cargar_paises()

    print("Sistema iniciado.")
    print(f"Paises cargados: {len(paises)}")

    while True:

        mostrar_menu()
        opcion = input("Ingrese una opcion: ")

        match opcion:
            case "1":
                agregar_pais(paises)
                guardar_paises(paises)

            case "2":
                actualizar_pais(paises)
                guardar_paises(paises)

            case "3":
                buscar_pais(paises)

            case "4":
                menu_filtros(paises)

            case "5":
                menu_ordenamientos(paises)

            case "6":
                mostrar_estadisticas(paises)

            case "0":
                guardar_paises(paises)
                print("Gracias por utilizar el sistema.")
                break

            case _:
                print("Opcion incorrecta. Intente nuevamente.")

if __name__ == "__main__":
    main()
