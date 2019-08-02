import csv 

with open("ejemplo.csv", 'w') as fcsv: # Creando archivo
    writer = csv.writer(fcsv) 
    writer.writerow(["Nombre", "Apellido", "Genero"]) 
    writer.writerow(["Nombre2", "Apellido2", "Genero2"]) 
    writer.writerow(["Nombre3", "Apellido3", "Genero3"]) 

with open("ejemplo.csv", 'r') as fcsv: # Leer archivo
    reader = csv.reader(fcsv) 
    for row in reader: 
        print(row) # Tipo lista
