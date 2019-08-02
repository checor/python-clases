import csv
import datetime

def agrega_hotel():
    nombre = input("Inserte nombre del hotel: ")
    ubicacion = input("Inserte ubicación: ")
    precio = input("Inserte precio por noche: ")
    fecha_actual = datetime.datetime.now()
    with open("hoteles.csv", "a") as fcsv:
        writer = csv.writer(fcsv)
        writer.writerow([nombre, ubicacion, precio, fecha_actual])


if __name__ == "__main__":
    cont = True
    while cont:
        agrega_hotel()
        c = input("Agregar otro hotel (s/N)? ")
        c = c.lower()
        if c.startswith("n") or c == "":
            cont = False
        elif c.startswith("s"):
            pass
        else:
            print("Comando no reconocido. Escriba si o no.")
        print("")

