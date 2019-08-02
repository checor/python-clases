cont  = True

while cont:
    nombre = input("Inserte nombre del hotel: ")
    ubicacion = input("Inserte ubicación: ")
    precio = input("Inserte precio por noche: ")
    with open("hoteles.txt", 'a') as hoteles_file:
        hoteles_file.write("{}\t{}\t{}\n".format(nombre, ubicacion, precio))
    valid = False
    while not valid:
        c = input("Agregar otro hotel (s/N)? ")
        c = c.lower()
        if c.startswith('s'):
            cont = True
            valid = True
        elif c.startswith('n'):
            cont = False
            valid = True
        else:
            print("Respuesta no válida")
            valid = False
    print("")
