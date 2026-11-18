# TPI-Python

# Gestión de Datos de Países en Python

## Descripción del proyecto

Este proyecto fue desarrollado como Trabajo Práctico Integrador de la materia **Programación 1**, correspondiente a la Tecnicatura Universitaria en Programación de la Universidad Tecnológica Nacional – Facultad Regional Mendoza.

El programa permite gestionar información de distintos países mediante una aplicación de consola desarrollada en Python.

Cada país contiene los siguientes datos:
- Nombre.
- Población.
- Superficie en kilómetros cuadrados.
- Continente.

La información se almacena en un archivo CSV, lo que permite conservar los datos entre distintas ejecuciones del programa.

## Funcionalidades principales

El sistema permite:

- **Agregar países:** incorporar nuevos países con sus respectivos datos.
- **Buscar países:** realizar búsquedas por nombre, admitiendo coincidencias parciales.
- **Actualizar información:** modificar la población y la superficie de un país existente.
- **Filtrar países:** consultar información según continente, rangos de población o rangos de superficie.
- **Ordenar información:** ordenar los países por nombre, población o superficie, de forma ascendente o descendente.
- **Consultar estadísticas:** obtener el país con mayor y menor población, promedios y cantidad de países por continente.
- **Guardar información:** almacenar los cambios en un archivo CSV.

## Tecnologías y herramientas utilizadas

- Python 3.
- Archivos CSV.
- Módulos y funciones.
- Listas y diccionarios.
- Git y GitHub.

## Estructura del proyecto

```text
Gestion_Paises/
│
├── main.py
├── paises.py
├── archivos.py
├── estadisticas.py
├── paises.csv
└── README.md
```

Descripción de los archivos:

| Archivo | Responsabilidad |
|---|---|
| `main.py` | Menú principal y coordinación del programa. |
| `paises.py` | Operaciones de búsqueda, carga, actualización, filtros y ordenamientos. |
| `archivos.py` | Lectura y escritura de los datos CSV. |
| `estadisticas.py` | Cálculo y presentación de estadísticas. |
| `paises.csv` | Archivo donde se almacenan los datos de los países. |

## Requisitos previos

Para ejecutar el programa se necesita:

- Tener instalado Python 3.
- Tener todos los archivos del proyecto dentro de una misma carpeta.
- Disponer del archivo `paises.csv`.

No se requieren librerías externas adicionales si se utiliza únicamente la biblioteca estándar de Python.

## Instrucciones de instalación y ejecución

1. Descargar o clonar el repositorio.
2. Abrir una terminal en la carpeta del proyecto.
3. Ejecutar el archivo principal con el siguiente comando:

```bash
python main.py
```

En algunos sistemas puede ser necesario utilizar:

```bash
python3 main.py
```

4. Una vez iniciado el programa, utilizar el menú de opciones para acceder a las distintas funcionalidades.

## Ejemplos de uso

### Ejemplo 1: búsqueda de un país

**Entrada:**

```text
Ingrese el nombre del país: arg
```

**Salida esperada:**

```text
País encontrado:
Nombre: Argentina
Población: [dato del archivo]
Superficie: [dato del archivo]
Continente: América
```

La búsqueda permite ingresar una parte del nombre del país.

### Ejemplo 2: ordenamiento por nombre

**Entrada:**

```text
Seleccione el criterio de ordenamiento: nombre
Seleccione el orden: ascendente
```

**Salida esperada:**

```text
Países ordenados por nombre:
Alemania
Argentina
Brasil
...
```

### Ejemplo 3: consulta de estadísticas

**Operación:** seleccionar la opción de estadísticas del menú principal.

**Resultados:** el programa presenta información como el país con mayor población, el país con menor población, los promedios y la cantidad de países por continente.

*Los valores concretos dependen de los datos almacenados en `paises.csv`.*

## Participación de los integrantes

**Brian Juan**
- Participación en el análisis y desarrollo del proyecto.
- Implementación y revisión de funcionalidades.
- Pruebas y validación del funcionamiento.
- Colaboración en la documentación.
- Participación en el análisis y desarrollo del proyecto.
- Implementación y revisión de funcionalidades.
- Pruebas y validación del funcionamiento.
- Colaboración en la documentación.

## Documentación del proyecto

**Informe final en PDF:**

[Juan_Brian_Informe_TPI_Gestion_de_Paises.pdf](https://github.com/user-attachments/files/35001488/Juan_Brian_Informe_TPI_Gestion_de_Paises.pdf)

El informe contiene la introducción, los objetivos, el marco teórico, las decisiones técnicas, el diagrama de flujo, las pruebas realizadas, las dificultades encontradas y las conclusiones.

## Video de presentación

**Video de demostración del proyecto:**
https://youtu.be/CSfQobwnjSE

El video presenta el funcionamiento general del programa y demuestra sus principales funcionalidades.

## Autor
- Brian Juan.


**Institución:** Universidad Tecnológica Nacional – Facultad Regional
