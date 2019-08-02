import sys
import csv
import json

def get_info(path, file_type):
    try:
        with open(path, 'r') as f:
            if file_type == 'json':
                datos = json.load(f)
                info = [[x['nombre'], x['ubicacion'], x['precio']] for x in datos]
            elif file_type == 'csv':
                reader = csv.reader(f)
                info = list(reader)
            elif file_type == 'txt':
                rows = list(f)
                info = []
                for row in rows:
                    info.append(row.split("\t"))
            else:
                raise TypeError("Unsupported file type")
    except:
        raise
    
    return info

def save_info(info, path, file_type):
    print(info)
    with open(path, 'w') as f:
        if file_type == 'json':
            datos = [{'nombre': x[0], 'ubicacion': x[1], 'precio': x[2]} for x in info ]
            json.dump(datos, f, indent=4)
        elif file_type == 'csv':
            writer = csv.writer(f)
            writer.writerows(info)
        elif file_type == 'txt':
            for row in info:
                f.writeline("\t".join(row))

def show_help():
    print("USO: conversor_hoteles.py [archivo_entrada] [tipo_entrada] [archivo_salida] [tipo_salida]")
    print("")
    print("archivo_entrada:  archivo con la info a convertir.")
    print("tipo_entrada:     tipo de archivo. csv, txt o json")
    print("archivo_salida:   archivo a guardar o sobreescribir.")
    print("tipo_salida:      tipo de archivo. csv, txt o json")

if __name__ == "__main__":
    if len(sys.argv) != 5 or "--help" in sys.argv:
        show_help()
        exit()
    supported_types = ('csv', 'txt', 'json')
    path1 = sys.argv[1]
    type1 = sys.argv[2].lower()
    if type1 not in supported_types:
        print("Tipo de archivo de entrada no soportado")
        exit()
    path2 = sys.argv[3]
    type2 = sys.argv[4]
    if type2 not in supported_types:
        print("Tipo de archivo de salida no soportado")
        exit()
    info = get_info(path1, type1)
    save_info(info, path2, type2)
