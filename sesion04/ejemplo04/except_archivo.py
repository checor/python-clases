import os
import sys

try:
    print(os.listdir(sys.argv[1]))
except FileNotFoundError:
    print("Error: Folder no existente")
except Exception as e:  # Se captura la excepción en una variable
    print("Error: {}".format(e))