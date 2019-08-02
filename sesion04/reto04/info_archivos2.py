import os
import sys
import json
from datetime import datetime

def obtiene_archivos(d):
    archivos = os.listdir(d)

    archivos = [
        {
            "nombre": a,
            "tamanio": os.path.getsize(os.path.join(d,a)),
            "fecha": os.path.getmtime(os.path.join(d,a)),
        }
        for a in archivos
    ]

    for archivo in archivos:
        fecha = datetime.fromtimestamp(archivo['fecha'])
        archivo['fecha'] = fecha.strftime("%c")


    archivos.sort(key=lambda a: a['tamanio'], reverse=True)

    return archivos

def imprime_archivos(archivos, print_json):
    if not print_json:
        print(archivos)
    else:
        archivos_json = json.dumps(archivos, indent=4)
        print(archivos_json)

if __name__ == "__main__":
    path = "."
    print_json = False
    if len(sys.argv) > 1:
        args = sys.argv[1:]
        for arg in args:
            if arg == '--json':
                print_json = True
            elif arg == '--help':
                print("Uso: info_archivos.py [PATH] [--json]")
                print("")
                print("PATH:   Carpeta a mostrar. Carpeta actual si no se coloca")
                print("--json: Imprime json. Diccionario si no se coloca.")
                exit()
            else:
                path = arg
    try:
        archivos = obtiene_archivos(path)
    except FileNotFoundError:
        print("Carpeta no existente!".format(path))
        exit()
    except NotADirectoryError:
        print("El path corresponde a un archivo, no a un directorio.")
        exit()
    imprime_archivos(archivos, print_json)