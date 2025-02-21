"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import pandas as pd
import re

def limpiar_linea(linea):
    return re.sub(r'\s+', ' ', linea.strip()).replace('.', '').strip()

def limpiar_encabezado(encabezados):
    return [encabezado.lower().replace(" ", "_") for encabezado in encabezados]

def procesar_valor(linea, valor_actual, filas):
    partes = re.split(r'\s{2,}', linea)
    if partes[0].isdigit():
        filas.append(valor_actual[:])
        valor_actual.clear()
        valor_actual.extend([
            int(partes[0]),
            int(partes[1]),
            float(partes[2].split()[0].replace(',', '.'))
        ])
        indice_porcentaje = linea.find('%')
        valor_actual.append(limpiar_linea(linea[indice_porcentaje + 1:]))
    else:
        valor_actual[-1] += " " + limpiar_linea(linea)

def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    with open("files/input/clusters_report.txt") as archivo:
        lineas = [linea.strip() for linea in archivo.readlines() if "---" not in linea]

    encabezado = re.split(r"\s{2,}", lineas[0])
    encabezado[1] += " palabras clave"
    encabezado[2] += " palabras clave"

    filas = []
    valor_actual = encabezado

    for linea in lineas[2:]:
        if linea:
            procesar_valor(linea, valor_actual, filas)

    filas.append(valor_actual)
    filas[0] = limpiar_encabezado(filas[0])

    df = pd.DataFrame(data=filas[1:], columns=filas[0])
    return df
