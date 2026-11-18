import csv
import os

ARCHIVO = "paises.csv"

def cargar_paises():
    paises = []

    if not os.path.exists(ARCHIVO):
        print("No se encontro el archivo CSV.")
        return paises

    try:
        with open(ARCHIVO, "r", encoding="utf-8", newline="") as archivo:
            lector = csv.DictReader(archivo)

            columnas = ["nombre","poblacion","superficie","continente"]

            if lector.fieldnames != columnas:
                print("Error: formato incorrecto del CSV.")
                return paises

            for numero, fila in enumerate(lector, start=2):
                try:
                    nombre =  fila["nombre"].strip()
                    poblacion = int(fila["poblacion"])
                    superficie = int(fila["superficie"])
                    continente = fila["continente"].strip()

                    if not nombre or not continente:
                        raise ValueError()

                    if poblacion <= 0 or superficie <=0:
                        raise ValueError()

                    pais = {
                        "nombre":nombre,
                        "poblacion":poblacion,
                        "superficie":superficie,
                        "continente":continente
                    }

                    paises.append(pais)

                except (ValueError, AttributeError, TypeError):
                    print(f"Registro invalido en la fila {numero}")

    except (OSError, csv.Error, UnicodeDecodeError):
        print("No se pudo leer correctamente el archivo.")

    return paises

def guardar_paises(paises):
    try:
        with open(ARCHIVO, "w", encoding="utf-8", newline="") as archivo:
            columnas = ["nombre","poblacion","superficie","continente"]

            escritor = csv.DictWriter(
                archivo,
                fieldnames=columnas
            )

            escritor.writeheader()
            escritor.writerows(paises)

        return True

    except (OSError, csv.Error):
        print("Error al guardar los datos.")
        return False