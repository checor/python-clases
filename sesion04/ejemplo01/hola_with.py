with open("hola2.txt", 'w') as archivo: 
    archivo.write("Primer linea de este archivo\n") 
    archivo.writelines(['Multiples Lineas\n', 'En Lista']) 
                                                                                                                                                 
with open("hola2.txt", 'r') as archivo: 
    print(archivo.readline()) 
    print(archivo.readlines())  
