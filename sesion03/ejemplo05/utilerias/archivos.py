"""Móudlo para mostrar una lista de archivos, con fecha y tamaño"""
import os
from datetime import datetime

def archivos(path="."):
    """Muestra la lista de archivos en el path, por defecto en la carpeta de trabajo"""
    files = os.listdir(path)
    sizes = [os.path.getsize(x) for x in files]
    dates = [os.path.getmtime(x) for x in files]

    data = list(zip(files, sizes, dates))
    data.sort(key = lambda x: x[1])

    print("-" * 80)
    print("{:<35}{:5}{:>39}".format("NOMBRE", "TAMAÑO", "FECHA"))
    print("-" * 80)
    for _file, size, timestamp in data:
        date = datetime.fromtimestamp(timestamp)
        print("{:<35}{:5}{:>40}".format(_file, size, date.strftime("%c")))
    print("-" * 80)

if __name__ == "__main__":
    archivos(".")