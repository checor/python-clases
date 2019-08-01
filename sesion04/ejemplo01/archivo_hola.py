# Escribiendo un archivo 

archivo = open("hola.txt", "w") # w para escritura

archivo.write("Primer linea de este archivo\n")
archivo.writelines(["Multiples ", "Linea\n", "En ", "Lista"])
archivo.close() # Debemos cerrar el archivo

# Leyendo un archivo
archivo = open("hola.txt", 'r')

archivo.readline()  
archivo.readlines()