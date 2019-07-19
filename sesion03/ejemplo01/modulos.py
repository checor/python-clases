# Importando algun modulo  
import os 

# Obteniendo ayuda
help(os)

# Lista de archivos
# q para salir, jk para moverse arriba / abajo
files = os.listdir()
print(files)

# Obteniendo el tamaño de un archivo    

size = os.path.getsize('manage.py')
print(size)

# Otras maneras de importar modulos
import os.path # Solo algun submodulo, llamando os.path
from os import path # Similar, se llama path directamente