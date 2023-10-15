#!/usr/bin/python3
"""Export data in CSV format"""
import csv
import requests
import sys


if __name__ == "__main__":
    """using REST API Placeholder through parameter"""
    parametro_id = sys.argv[1]

    url = f"https://jsonplaceholder.typicode.com/todos?userId={parametro_id}"
    url_nombre = f"https://jsonplaceholder.typicode.com/users/{parametro_id}"

    respuesta = requests.get(url)
    respuesta_nombre = requests.get(url_nombre)

    total_tarea = respuesta.json()
    informacion_empleado = respuesta_nombre.json()

    formato_archivo = parametro_id + ".csv"
    with open(formato_archivo, mode='w', newline="") as file:
        contenedor = []
        for tarea in total_tarea:
            formato = [
                "{}".format(parametro_id),
                "{}".format(informacion_empleado.get("username")),
                "{}".format(tarea.get("completed")),
                "{}".format(tarea.get("title"))
            ]
            contenedor.append(formato)
        escritor_csv = csv.writer(file, quoting=csv.QUOTE_ALL)
        escritor_csv.writerows(contenedor)
        print("creado con exito ")
