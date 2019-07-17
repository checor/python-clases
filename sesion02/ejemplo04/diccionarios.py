# Creando diccionarios  
d1 = {}
d2 = dict() 

print(type(d1) )


d3 = {"Calle": "Monte de las cruces", "Tel": "+555555501", "Ciudad": "Tijuana"} 
d4 = {"Medicamento": "Paracetamol", "Dosis": 8}                          

print(d3)
print(d4)

print(d3.keys()) # Lista de llaves
print(d4.values()) # Lista de valores

for item, value in d3.items():  # Accediendo mediante for
    print(item, ":", value) 
