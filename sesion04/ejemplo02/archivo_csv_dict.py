import csv

with open("ejemplod.csv", 'w') as fcsv: 
    fields = ("Nombre", "Apellido", "Edad") 
    writer = csv.DictWriter(fcsv, fieldnames=fields)
    writer.writeheader() 
    writer.writerow({'Nombre': 'Pedro', 'Apellido': 'Picapiedra', 'Edad': 30}) 
    writer.writerow({'Nombre': 'Pablo', 'Apellido': 'Marmol', 'Edad': 29}) 

with open("ejemplod.csv", 'r') as fcsv: 
    reader = csv.DictReader(fcsv) 
    for row in reader: 
        print(row['Nombre'], row['Apellido'])